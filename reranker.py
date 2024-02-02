# coding=utf-8
import logging
from typing import List, Optional, Union

import torch

DEFAULT_TEXT_RERANK_TMPL = "context: {context}\n\nCan you find some useful information in the previous context that can help you answer the following question? \nquestion: {query}.\n\nAnswer only with 'Yes' or 'No', don't say anything else !!"

class Reranker:
    def __init__(
        self,
        model_name_or_path: str,
        model_kwargs: Optional[dict] = None,
        tokenizer_kwargs: Optional[dict] = None,
        device: Union[torch.device, str, int] = "cpu",
    ):
        model_kwargs = model_kwargs or {}
        tokenizer_kwargs = tokenizer_kwargs or {}
        try:
            from transformers import AutoModelForCausalLM, AutoTokenizer
        except ImportError as exc:
            raise ImportError(
                f"{type(self).__class__} requires torch and transformers packages.\n"
                "Please install both with `pip install transformers[torch]`."
            ) from exc

        self._tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, **tokenizer_kwargs)
        self._tokenizer.add_special_tokens({"pad_token": "<s>"})
        self._model = AutoModelForCausalLM.from_pretrained(model_name_or_path, **model_kwargs).to(device)

        self._no_id = self._tokenizer.encode("No")[-1]
        self._yes_id = self._tokenizer.encode("Yes")[-1]

    def _predict(self, query, contexts):
        inputs = [DEFAULT_TEXT_RERANK_TMPL.format(query=query, context=context) for context in contexts]
        inputs_messages = [
            self._tokenizer.apply_chat_template([{"role": "user", "content": input}], tokenize=False) for input in inputs
        ]
        tokens = self._tokenizer(inputs_messages, return_tensors="pt", padding=True).to(self._model.device)

        with torch.no_grad():
            out = self._model(tokens["input_ids"])

        return [(out["logits"][i][-1][self._no_id] < out["logits"][i][-1][self._yes_id]).item() for i in range(out["logits"].shape[0])]

    def __call__(self, query: str, documents: List):
        document_texts = [doc.text for doc in documents]
        is_validated = self._predict(query, document_texts)

        retrieved_documents = [doc for doc, is_validated_ in zip(documents, is_validated) if is_validated_]
        logging.info(f"{self.__class__} retrieved {len(retrieved_documents)} documents from {len(documents)}")

        return retrieved_documents
