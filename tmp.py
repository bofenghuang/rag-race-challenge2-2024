#!/usr/bin/env python
# coding=utf-8
# Copyright 2023  Bofeng Huang
# Uncomment if necessary
import os

os.environ["HF_HOME"] = "/projects/bhuang/.cache/huggingface"
# os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["BITSANDBYTES_NOWELCOME"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "1,2"

import logging
import sys
import json

import torch
from llama_index import ServiceContext, SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms import HuggingFaceLLM
from llama_index.indices.struct_store import JSONQueryEngine
from llama_index.prompts import PromptTemplate
from llama_index.embeddings import HuggingFaceEmbedding

def jload(json_file):
    with open(json_file) as f:
        return json.load(f)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# load documents
# documents = SimpleDirectoryReader("./data/paul_graham/").load_data()

# This will wrap the default prompts that are internal to llama-index
# query_wrapper_prompt = PromptTemplate(
#     "Below is an instruction that describes a task. "
#     "Write a response that appropriately completes the request.\n\n"
#     "### Instruction:\n{query_str}\n\n### Response:"
# )

# load embedding model
embed_model_name_or_path = "intfloat/multilingual-e5-large"
embed_model = HuggingFaceEmbedding(
    model_name=embed_model_name_or_path,
    # embed_batch_size=
)

# load llm
llm_model_name_or_path = "mistralai/Mistral-7B-Instruct-v0.2"
# llm_model_name_or_path = "mistralai/Mixtral-8x7B-Instruct-v0.1"

query_wrapper_prompt = PromptTemplate(
    "<s> [INST] {query_str} [/INST]"
)

llm = HuggingFaceLLM(
    context_window=32768,
    max_new_tokens=1024,
    generate_kwargs={"temperature": 0, "do_sample": False},
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name=llm_model_name_or_path,
    model_name=llm_model_name_or_path,
    device_map="auto",
    tokenizer_kwargs={"max_length": 32768},
    # uncomment this if using CUDA to reduce memory usage
    model_kwargs={"torch_dtype": torch.float16},
)
service_context = ServiceContext.from_defaults(
    # chunk_size=512,
    embed_model="local",
    llm=llm,
)

# index = VectorStoreIndex.from_documents(
#     documents, service_context=service_context
# )

# query_engine = index.as_query_engine()
# response = query_engine.query("What did the author do growing up?")

input_json_file = "/home/bhuang/nlp/rag-race-challenge2-2024/data/sources_sample/Twitter_APIv2-Usage.json"
schema_json_file = "/home/bhuang/nlp/rag-race-challenge2-2024/data/schema.json"
json_value = jload(input_json_file)
json_schema = jload(schema_json_file)

nl_query_engine = JSONQueryEngine(
    json_value=json_value,
    json_schema=json_schema,
    service_context=service_context,
)
nl_response = nl_query_engine.query("What comments has Jerry been writing?")
print(nl_response)
