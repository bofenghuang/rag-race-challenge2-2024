#!/usr/bin/env python
# coding=utf-8

from typing import TYPE_CHECKING, Any, List, Optional, Sequence, Union

from llama_index.bridge.pydantic import Field
from llama_index.core.embeddings.base import (
    DEFAULT_EMBED_BATCH_SIZE,
    BaseEmbedding,
    Embedding,
)
from llama_index.utils import get_cache_dir, infer_torch_device

DEFAULT_HUGGINGFACE_LENGTH = 512


class HuggingFaceEmbedding(BaseEmbedding):
    max_length: int = Field(default=DEFAULT_HUGGINGFACE_LENGTH, description="Maximum length of input.", gt=0)

    def __init__(
        self,
        model_name: str = "BAAI/bge-m3",
        pooling: str = "cls",
        use_fp16: bool = True,
        max_length: Optional[int] = None,
        embed_batch_size: int = DEFAULT_EMBED_BATCH_SIZE,
        device: Optional[str] = None,
        **kwargs,
    ):
        try:
            from FlagEmbedding import BGEM3FlagModel
        except ImportError:
            raise ImportError("Please install FlagEmbedding with `pip install -U FlagEmbedding`.")

        self._device = device or infer_torch_device()
        self._model = BGEM3FlagModel(model_name, pooling_method=pooling, use_fp16=use_fp16, device=self._device)

        super().__init__(embed_batch_size=embed_batch_size, max_length=max_length, **kwargs)

    @classmethod
    def class_name(cls) -> str:
        return "FlagEmbedding"

    def _embed(
        self,
        sentences: List[str],
        return_dense: bool = True,
        return_sparse: bool = True,
        return_colbert_vecs: bool = True,
    ) -> List[List[float]]:
        embeddings = self._model(
            sentences,
            batch_size=self.embed_batch_size,
            max_length=self.max_length,
            return_dense=return_dense,
            return_sparse=return_sparse,
            return_colbert_vecs=return_colbert_vecs,
        )

        return embeddings.tolist()

    def _get_query_embedding(self, query: str) -> List[float]:
        """Get query embedding."""
        # query = format_query(query, self.model_name, self.query_instruction)
        return self._embed([query])[0]

    async def _aget_query_embedding(self, query: str) -> List[float]:
        """Get query embedding async."""
        return self._get_query_embedding(query)

    async def _aget_text_embedding(self, text: str) -> List[float]:
        """Get text embedding async."""
        return self._get_text_embedding(text)

    def _get_text_embedding(self, text: str) -> List[float]:
        """Get text embedding."""
        # text = format_text(text, self.model_name, self.text_instruction)
        return self._embed([text])[0]

    def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Get text embeddings."""
        # texts = [format_text(text, self.model_name, self.text_instruction) for text in texts]
        return self._embed(texts)
