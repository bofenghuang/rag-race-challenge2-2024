# coding=utf-8

import logging
import re
import string
from typing import Callable, Dict, List, Optional

from llama_index.retrievers import BaseRetriever
from llama_index.retrievers.bm25_retriever import tokenize_remove_stopwords

EPS = 1e-5


# simple_tokenizer = lambda x: x.split(" ")
def simple_tokenizer(s):
    s = s.lower().strip()
    s = re.sub(rf"(?<=\w)([{re.escape(string.punctuation)}]+)(?=\s|$)", r" \1", s)
    s = re.split(r"\s+", s)
    return s


class BM25CategoryRetriever:
    def __init__(
        self,
        corpus: List[str],
        categories: Optional[List[str]] = None,
        tokenizer: Optional[Callable[[str], List[str]]] = None,
        top_k: int = 1,
    ):
        try:
            from rank_bm25 import BM25Okapi
        except ImportError:
            raise ImportError("Please install rank_bm25: pip install rank-bm25")

        self._tokenizer = tokenizer or tokenize_remove_stopwords
        self._top_k = top_k
        self._categories = corpus if categories is None else categories
        self._corpus = [self._tokenizer(c) for c in corpus]
        self.bm25 = BM25Okapi(self._corpus)

    def _retrieve(self, query: str):
        tokenized_query = self._tokenizer(query)
        doc_scores = self.bm25.get_scores(tokenized_query)
        sorted_doc_scores = sorted(enumerate(doc_scores), key=lambda x: x[1], reverse=True)
        sorted_doc_scores = [(self._categories[idx_], doc_score_) for idx_, doc_score_ in sorted_doc_scores]
        # remove 0 prediction
        sorted_doc_scores = [doc_store_ for doc_store_ in sorted_doc_scores if doc_store_[1] > EPS]
        return sorted_doc_scores[: self._top_k], doc_scores.sum()

    def __call__(
        self,
        query: str,
        documents: List[Dict],
    ):
        doc_scores, _ = self._retrieve(query)
        selected_categories = [doc_score_[0] for doc_score_ in doc_scores]
        logging.info(f"Selected the following categories: {selected_categories}")

        return [doc for doc in documents if doc.metadata["platform"] in selected_categories], selected_categories


class ModerateBM25CategoryRetriever(BM25CategoryRetriever):
    def __init__(self, corpus: List[str], name_mapping: Optional[dict] = None, **kwargs):
        if name_mapping is not None:
            mapped_corpus = [name_mapping.get(c.lower()) if name_mapping.get(c.lower()) else c for c in corpus]
        self._name_mapping = name_mapping
        super().__init__(corpus=mapped_corpus, categories=corpus, **kwargs)

    def _retrieve(self, query: str):
        doc_scores, score_sum = super()._retrieve(query)

        if score_sum < EPS and self._name_mapping is not None:
            for k, v in self._name_mapping.items():
                query = re.sub(rf"\b{k}\b", v, query, flags=re.IGNORECASE)
            doc_scores, score_sum = super()._retrieve(query)

        assert score_sum > EPS, query
        return doc_scores, score_sum


class NotHardRetriever(BaseRetriever):
    def __init__(
        self,
        vector_retrievers,
        #  bm25_retriever
    ):
        self._documents = list(vector_retrievers.keys())
        # debug
        self._documents += ["Booking.com", "Facebook", "Linkedin", "Pinterest", "Tiktok"]

        self.document_retriever = ModerateBM25CategoryRetriever(
            self._documents,
            name_mapping={"x": "x twitter tweet", "booking.com": "booking", "facebook": "facebook meta"},  # todo
            similarity_top_k=1,
        )

        self.vector_retrievers = vector_retrievers
        # self.bm25_retriever = bm25_retriever
        super().__init__()

    def _retrieve(self, query, **kwargs):

        # 1best
        document_id, _ = self.document_retriever(query.query_str)[0]
        document = self._documents[document_id]
        logging.info(f"Selected document {document}")

        # bm25_retriever = self.bm25_retriever[document]
        vector_retriever = self.vector_retrievers[document]

        # bm25_nodes = bm25_retriever.retrieve(query, **kwargs)
        vector_nodes = vector_retriever.retrieve(query, **kwargs)

        return vector_nodes

        # combine the two lists of nodes
        all_nodes = []
        node_ids = set()
        for n in bm25_nodes + vector_nodes:
            if n.node.node_id not in node_ids:
                all_nodes.append(n)
                node_ids.add(n.node.node_id)
        return all_nodes
