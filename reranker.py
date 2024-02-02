from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


def apply_template(query, context):
    return f"context: {context}\n\nCan you find some useful information in the previous context that can help you answer the following question? \nquestion: {query}.\n\nAnswer only with 'Yes' or 'No', don't say anything else !!"


class Reranker:
    def __init__(self, model_path, device):
        self.model = AutoModelForCausalLM.from_pretrained(model_path).to(device)

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.device = device
        
    def validate(self, query, contexts):
        inputs = [apply_template(query, context) for context in contexts]
        inputs_messages = [
            self.tokenizer.apply_chat_template(
                [{"role": "user", "content": input}], tokenize=False
            )
            for input in inputs
        ]
        self.tokenizer.add_special_tokens({"pad_token": "<s>"})
        tokens = self.tokenizer(inputs_messages, return_tensors="pt", padding=True).to(
            self.device
        )

        no_id = self.tokenizer.encode("No")[-1]
        yes_id = self.tokenizer.encode("Yes")[-1]

        with torch.no_grad():
            out = self.model(tokens["input_ids"])

        return [
            (out["logits"][i][-1][no_id] < out["logits"][i][-1][yes_id]).item()
            for i in range(out["logits"].shape[0])
        ]
