# coding=utf-8

import logging
from functools import partial
from typing import Any, Dict, List

import datasets
import numpy as np
import torch
from FlagEmbedding import BGEM3FlagModel
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import BatchEncoding, DataCollatorWithPadding, PreTrainedTokenizerFast

# from FlagEmbedding.bge_m3 import _transform_func


def _transform_func(
    examples: Dict[str, List],
    tokenizer: PreTrainedTokenizerFast,
    max_length: int = 8192,
) -> BatchEncoding:
    inputs = tokenizer(
        examples["text"],
        max_length=max_length,
        padding="max_length",  # todo: slow down
        return_token_type_ids=False,
        truncation=True,
        return_tensors="pt",
    )
    return inputs


def _compute_similarity(q_reps: torch.Tensor, p_reps: torch.Tensor):
    return torch.matmul(q_reps, p_reps.transpose(-2, -1))


def _compute_dense_score(q_reps: torch.Tensor, p_reps: torch.Tensor):
    scores = _compute_similarity(q_reps, p_reps)
    scores = scores.view(q_reps.size(0), -1)
    return scores


def _compute_sparse_score(q_reps: torch.Tensor, p_reps: torch.Tensor):
    scores = _compute_similarity(q_reps, p_reps)
    scores = scores.view(q_reps.size(0), -1)
    return scores


def _compute_colbert_score(q_reps: torch.Tensor, p_reps: torch.Tensor, q_mask: torch.Tensor = None):
    token_scores = torch.einsum("qin,pjn->qipj", q_reps, p_reps)
    scores, _ = token_scores.max(-1)
    # scores = scores.sum(1) / q_mask[:, 1:].sum(-1, keepdim=True)
    scores = scores.sum(1) / q_reps.shape[1]
    return scores


def compute_scores(
    q_embeddings: Dict[str, np.ndarray],
    p_embeddings: Dict[str, np.ndarray],
    # device: Union[torch.device, str, int] = "cpu",
    weights_for_different_modes: List[float] = None,
):
    # q_embeddings = {k: torch.from_numpy(v).to(device) for k, v in q_embeddings.items()}
    # p_embeddings = {k: torch.from_numpy(v).to(device) for k, v in p_embeddings.items()}

    dense_score = _compute_dense_score(q_embeddings["dense_embedding"], p_embeddings["dense_embedding"])
    dense_score = dense_score.cpu().numpy()

    sparse_score = _compute_sparse_score(q_embeddings["sparse_embedding"], p_embeddings["sparse_embedding"])
    sparse_score = sparse_score.cpu().numpy()

    colbert_score = _compute_colbert_score(q_embeddings["colbert_embedding"], p_embeddings["colbert_embedding"])
    colbert_score = colbert_score.cpu().numpy()

    if weights_for_different_modes is None:
        weights_for_different_modes = [1, 1.0, 1.0]
        print("default weights for dense, sparse, colbert are [1.0, 1.0, 1.0] ")
    else:
        assert len(weights_for_different_modes) == 3

    sparse_dense_score = (dense_score * weights_for_different_modes[0] + sparse_score * weights_for_different_modes[1]) / sum(
        weights_for_different_modes[:2]
    )

    colbert_sparse_dense_score = (
        dense_score * weights_for_different_modes[0]
        + sparse_score * weights_for_different_modes[1]
        + colbert_score * weights_for_different_modes[2]
    ) / sum(weights_for_different_modes)

    return {
        "dense_score": dense_score,
        "sparse_score": sparse_score,
        "colbert_score": colbert_score,
        "sparse_dense_score": sparse_dense_score,
        "colbert_sparse_dense_score": colbert_sparse_dense_score,
    }


class BGEM3EmbedModel(BGEM3FlagModel):

    @torch.no_grad()
    def embed_single(
        self,
        sentence: str,
        max_length: int = 8192,
        return_dense: bool = True,
        return_sparse: bool = True,
        return_colbert_vecs: bool = True,
        return_sparse_embedding: bool = True,
    ):
        sentences = [sentence]

        def _tokenize(texts: list, max_length: int):
            return self.tokenizer(
                texts, max_length=max_length, padding=True, return_token_type_ids=False, truncation=True, return_tensors="pt"
            )

        self.model.eval()

        tokenized_input = _tokenize(sentences, max_length=max_length).to(self.device)

        output = self.model(
            tokenized_input,
            return_dense=return_dense,
            return_sparse=return_sparse,
            return_colbert=return_colbert_vecs,
            return_sparse_embedding=return_sparse_embedding,
        )

        dense_embedding, sparse_embedding, colbert_embedding = [], [], []

        if return_dense:
            # dense_embedding = output["dense_vecs"].float().cpu().numpy()
            dense_embedding = output["dense_vecs"].float()

        if return_sparse:
            # sparse_embedding = output["sparse_vecs"].float().cpu().numpy()
            sparse_embedding = output["sparse_vecs"].float()

        if return_colbert_vecs:
            # colbert_embedding = output["colbert_vecs"].float().cpu().numpy()
            colbert_embedding = output["colbert_vecs"].float()

        return {
            "dense_embedding": dense_embedding,
            "sparse_embedding": sparse_embedding,
            "colbert_embedding": colbert_embedding,
        }

    @torch.no_grad()
    def embed_multi(
        self,
        sentences: List[str],
        batch_size: int = 12,
        max_length: int = 8192,
        return_dense: bool = True,
        return_sparse: bool = True,
        return_colbert_vecs: bool = True,
        return_sparse_embedding: bool = True,
    ) -> Dict:

        if self.num_gpus > 1:
            batch_size *= self.num_gpus
        self.model.eval()

        dataset = datasets.Dataset.from_dict({"text": sentences})
        dataset.set_transform(partial(_transform_func, tokenizer=self.tokenizer, max_length=max_length))

        data_collator = DataCollatorWithPadding(self.tokenizer)
        data_loader = DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=False,
            drop_last=False,
            num_workers=4,
            collate_fn=data_collator,
        )

        all_dense_embeddings, all_sparse_embeddings, all_colbert_embeddings = [], [], []
        for batch_data in tqdm(data_loader, desc="generate embeddings", mininterval=10):
            batch_data = batch_data.to(self.device)

            output = self.model(
                batch_data,
                return_dense=return_dense,
                return_sparse=return_sparse,
                return_colbert=return_colbert_vecs,
                return_sparse_embedding=return_sparse_embedding,
            )
            if return_dense:
                # all_dense_embeddings.append(output["dense_vecs"].float().cpu().numpy())
                all_dense_embeddings.extend(list(output["dense_vecs"].float()))

            if return_sparse:
                # all_sparse_embeddings.append(output["sparse_vecs"].float().cpu().numpy())
                all_sparse_embeddings.extend(list(output["sparse_vecs"].float()))

            if return_colbert_vecs:
                # all_colbert_embeddings.append(output["colbert_vecs"].float().cpu().numpy())
                all_colbert_embeddings.extend(list(output["colbert_vecs"].float()))

        # if return_dense:
        #     all_dense_embeddings = np.concatenate(all_dense_embeddings, axis=0)

        # if return_sparse:
        #     all_sparse_embeddings = np.concatenate(all_sparse_embeddings, axis=0)

        # if return_colbert_vecs:
        #     all_colbert_embeddings = np.concatenate(all_colbert_embeddings, axis=0)

        return {
            "dense_embedding": all_dense_embeddings,
            "sparse_embedding": all_sparse_embeddings,
            "colbert_embedding": all_colbert_embeddings,
        }


class BGEM3EmbedDocumentRetriever:
    def __init__(
        self,
        model: Any,
        batch_size: int = 12,
        max_query_length: int = 512,
        max_document_length: int = 512,
        weights_for_different_modes: List[float] = None,
        score_name: str = "dense_score",
        top_k: int = 50,
    ):
        self.model = model
        self._batch_size = batch_size
        self._max_query_length = max_query_length
        self._max_document_length = max_document_length
        self._weights_for_different_modes = weights_for_different_modes
        self._score_name = score_name
        self._top_k = top_k

    def embed_query(self, query: str):
        return self.model.embed_single(query, max_length=self._max_query_length)

    def embed_documents(self, documents: List[Dict], **kwargs):
        # embed with augmented text (metadata, summary, etc)
        sentences = [doc.text_with_metadata for doc in documents]
        embeddings = self.model.embed_multi(
            sentences, batch_size=self._batch_size, max_length=self._max_document_length, **kwargs
        )

        # documents = [{**doc, **{k: v[idx] for k, v in embeddings.items()}} for idx, doc in enumerate(documents)]
        for idx, doc in enumerate(documents):
            for k, v in embeddings.items():
                # doc.__setattr__(k, v[idx])
                setattr(doc, k, v[idx])
            documents[idx] = doc

        return documents

    def __call__(self, query: str, documents: List[Dict]):
        query_embedding = self.embed_query(query)
        embed_names = query_embedding.keys()

        document_embeddings = {
            embed_name: torch.stack([getattr(doc, embed_name) for doc in documents], axis=0) for embed_name in embed_names
        }

        output = compute_scores(
            query_embedding, document_embeddings, weights_for_different_modes=self._weights_for_different_modes
        )
        scores = output[self._score_name][0]

        sorted_result_tups = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
        sorted_result_tups = sorted_result_tups[: self._top_k]
        # result_ids, result_similarities = list(zip(*sorted_result_tups))
        # retrieved_documents = [documents[idx] for idx in result_ids]

        retrieved_documents = []
        for idx, sim in sorted_result_tups:
            doc = documents[idx]
            doc.embed_score = sim
            retrieved_documents.append(doc)

        # remove embedding
        # retrieved_documents = [{k: v for k, v in doc if k not in embed_names} for doc in retrieved_documents]
        logging.info(f"{self.__class__} retrieved {len(retrieved_documents)} documents from {len(documents)}")

        return retrieved_documents
