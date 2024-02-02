# coding=utf-8

class HuggingFaceLLM:
    def _load_model(
            self,
            model_name,
            context_window,
            max_new_tokens,
            system_prompt,
            ):

    try:
        import torch
        from transformers import (
            AutoModelForCausalLM,
            AutoTokenizer,
            StoppingCriteria,
            StoppingCriteriaList,
        )
    except ImportError as exc:
        raise ImportError(
            f"{type(self).__name__} requires torch and transformers packages.\n"
            "Please install both with `pip install transformers[torch]`."
        ) from exc
    
        self._model = model or AutoModelForCausalLM.from_pretrained(
        model_name, device_map=device_map, **model_kwargs
    )