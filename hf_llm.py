# coding=utf-8

from typing import Optional
import torch


class HuggingFaceLLM:
    def __init__(self, **kwargs) -> None:
        self._load_model(**kwargs)

    def _load_model(
        self,
        model_name,
        # context_window,
        # max_new_tokens,
        # system_prompt,
        device_map: Optional[str] = "auto",
        model_kwargs: Optional[dict] = None,
        tokenizer_kwargs: Optional[dict] = None,
        generate_kwargs: Optional[dict] = None,
        query_wrapper_prompt: str = "{query}",
    ):

        model_kwargs = model_kwargs or {}
        tokenizer_kwargs = tokenizer_kwargs or {}
        generate_kwargs = generate_kwargs or {}

        try:
            from transformers import (
                AutoModelForCausalLM,
                AutoTokenizer,
                StoppingCriteria,
                StoppingCriteriaList,
            )
        except ImportError as exc:
            raise ImportError(
                f"{type(self).__class__} requires torch and transformers packages.\n"
                "Please install both with `pip install transformers[torch]`."
            ) from exc

        self._tokenizer = AutoTokenizer.from_pretrained(model_name, **tokenizer_kwargs)
        self._model = AutoModelForCausalLM.from_pretrained(model_name, device_map=device_map, **model_kwargs)

        self._generate_kwargs = generate_kwargs
        self._query_wrapper_prompt = query_wrapper_prompt

    def _predict(self, query):
        full_prompt = self._query_wrapper_prompt.format(query=query)

        inputs = self._tokenizer(full_prompt, return_tensors="pt")
        inputs = inputs.to(self._model.device)

        tokens = self._model.generate(
            **inputs,
            # max_new_tokens=self.max_new_tokens,
            # stopping_criteria=self._stopping_criteria,
            **self._generate_kwargs,
        )
        completion_tokens = tokens[0][inputs["input_ids"].size(1) :]
        completion = self._tokenizer.decode(completion_tokens, skip_special_tokens=True)

        return completion


# llm_model_name_or_path = "mistralai/Mistral-7B-Instruct-v0.2"
# # llm_model_name_or_path = "mistralai/Mixtral-8x7B-Instruct-v0.1"
# # llm_model_name_or_path = "microsoft/phi-2"

# query_wrapper_prompt = "<s>[INST] {query} [/INST]"
# # query_wrapper_prompt = "Instruct: {query}\nOutput: "

# model = HuggingFaceLLM(
#     model_name=llm_model_name_or_path,
#     device_map="auto",
#     # device_map="sequential",
#     # uncomment this if using CUDA to reduce memory usage
#     model_kwargs={
#         "torch_dtype": torch.float16,
#         # "max_memory": {0: '40GiB', 1: '40GiB', 2: '40GiB'},
#     },
#     tokenizer_kwargs={"max_length": 32768},
#     generate_kwargs={"max_new_tokens": 256, "temperature": 0, "do_sample": False},
#     query_wrapper_prompt=query_wrapper_prompt,
# )

# query = "How is content moderation carried out on X?"
# r = model._predict(query)
# print(r)
