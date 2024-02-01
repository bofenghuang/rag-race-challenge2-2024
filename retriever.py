#!/usr/bin/env python
# coding=utf-8

import re
import string
from typing import Callable, List, Optional

from llama_index.retrievers import BaseRetriever
from llama_index.retrievers.bm25_retriever import tokenize_remove_stopwords


# simple_tokenizer = lambda x: x.split(" ")
def simple_tokenizer(s):
    s = s.lower().strip()
    s = re.sub(rf"(?<=\w)([{re.escape(string.punctuation)}]+)(?=\s|$)", r" \1", s)
    s = re.split(r"\s+", s)
    return s


class BM25Classifier:
    def __init__(
        self,
        corpus: List[str],
        tokenizer: Optional[Callable[[str], List[str]]] = None,
        similarity_top_k: int = 1,
    ):
        try:
            from rank_bm25 import BM25Okapi
        except ImportError:
            raise ImportError("Please install rank_bm25: pip install rank-bm25")

        self._tokenizer = tokenizer or tokenize_remove_stopwords
        self._similarity_top_k = similarity_top_k
        self._corpus = [self._tokenizer(c) for c in corpus]
        self.bm25 = BM25Okapi(self._corpus)

    def __call__(self, query: str):
        tokenized_query = self._tokenizer(query)
        doc_scores = self.bm25.get_scores(tokenized_query)
        return sorted(enumerate(doc_scores), key=lambda x: x[1])[::-1][: self._similarity_top_k], doc_scores.sum()


class DocumentBM25Classifier(BM25Classifier):
    def __init__(self, corpus: List[str], name_mapping: Optional[dict] = None, **kwargs):
        if name_mapping is not None:
            corpus = [name_mapping.get(c.lower()) if name_mapping.get(c.lower()) else c for c in corpus]
        self._name_mapping = name_mapping
        super().__init__(corpus=corpus, **kwargs)

    def __call__(self, query: str):
        nbest, score_sum = super().__call__(query)
        if score_sum < 1e-5 and self._name_mapping is not None:
            for k, v in self._name_mapping.items():
                query = re.sub(rf"\b{k}\b", v, query, flags=re.IGNORECASE)
            nbest, score_sum = super().__call__(query)

        assert score_sum > 1e-5, query
        return nbest


class NotHardRetriever(BaseRetriever):
    def __init__(
        self,
        vector_retrievers,
        #  bm25_retriever
    ):
        self._documents = vector_retrievers.keys()

        self.document_retriever = DocumentBM25Classifier(
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

        # bm25_retriever = self.bm25_retriever[document]
        vector_retrievers = self.vector_retrievers[document]

        # bm25_nodes = bm25_retriever.retrieve(query, **kwargs)
        vector_nodes = vector_retrievers.retrieve(query, **kwargs)

        # combine the two lists of nodes
        all_nodes = []
        node_ids = set()
        for n in bm25_nodes + vector_nodes:
            if n.node.node_id not in node_ids:
                all_nodes.append(n)
                node_ids.add(n.node.node_id)
        return all_nodes
