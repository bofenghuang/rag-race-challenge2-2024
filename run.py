#!/usr/bin/env python
# coding=utf-8

import os

os.environ["HF_HOME"] = "/projects/bhuang/.cache/huggingface"
# os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["BITSANDBYTES_NOWELCOME"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,2,3,4,5"
# os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

import json
import pandas as pd
import logging
import sys
from collections import defaultdict
from pathlib import Path
import torch


from reader import NotSimpleDirectoryReader, get_file_metadata
from category_retriever import ModerateBM25CategoryRetriever
from embed_retriever import BGEM3EmbedModel, BGEM3EmbedDocumentRetriever
from simple_reader import SimplerReader
from hf_llm import HuggingFaceLLM

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

input_csv_file = (
    "/home/bhuang/nlp/rag-race-challenge2-2024/challenge-2-dataset-and-documentation/dataset/train/input/questions.csv"
)

# input_dir = "/home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions"
input_dir = "/home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions-sample"

df = pd.read_csv(input_csv_file, sep=";")
queries = df["question"].tolist()

# load documents

documents, documents_chunks, documents_smaller_chunks, documents_smaller_smaller_chunks, smallest_chunks = SimplerReader(
    input_dir
).load_files()

docs = smallest_chunks

"""
documents = NotSimpleDirectoryReader(
    input_dir=input_dir,
    exclude=["README.md"],
    recursive=True,
    required_exts=[".md"],
    # file_extractor
    file_metadata=get_file_metadata,
).load_data()

text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        # First, try to split along Markdown headings (starting with level 2)
        # "\n#{1,6} ",
        "\n#{1,3} ",
        # Note the alternative syntax for headings (below) is not handled here
        # Heading level 2
        # ---------------
        # End of code block
        # "```\n",
        # Horizontal lines
        # "\n\\*\\*\\*+\n",
        # "\n---+\n",
        # "\n___+\n",
        # Note that this splitter doesn't handle horizontal lines defined
        # by *three or more* of ***, ---, or ___, but this is not handled
        "\n" * 4,
        # "\n\n",
        # "\n",
        # " ",
        # "",
    ],
    chunk_size=1024,
    chunk_overlap=0,
    is_separator_regex=True,
)
text_splitter = LangchainNodeParser(text_splitter)

nodes = text_splitter.get_nodes_from_documents(documents)

docs = [
    {
        "text": n.get_content("all"),
        "platform": n.metadata["platform"],
    }
    for n in nodes
]
"""

doc_names = list(set([d.metadata["platform"] for d in docs]))

category_document_retriever = ModerateBM25CategoryRetriever(
    doc_names,
    name_mapping={"x": "x twitter tweet", "booking.com": "booking", "facebook": "facebook meta"},  # todo
    top_k=2,
)

# Setting use_fp16 to True speeds up computation with a slight performance degradation
embed_model = BGEM3EmbedModel("BAAI/bge-m3", use_fp16=True, device=3)
embed_document_retriever = BGEM3EmbedDocumentRetriever(
    embed_model,
    batch_size=12,
    max_query_length=512,
    max_document_length=512,
    # score_name="dense_score",
    # score_name = "sparse_dense_score",
    score_name="colbert_sparse_dense_score",
    # weights_for_different_modes = None,  # todo: 
    top_k=5,
)

docs = embed_document_retriever.embed_documents(docs)

# -- query stage

# query = "How is content moderation carried out on X?"
query = "How is content moderation carried out on twitter?"
# query = "I have access to a set of tweets URLs that I consider to be hateful. How can I use Twitter's API to monitor the average duration between the tweet's creation and its moderation?"

docs_, _ = category_document_retriever(query, docs)

docs_ = embed_document_retriever(query, docs_)
print(docs_)

# debug
# data = [{"query": query, "catgory": category_document_retriever(query, docs)[1]} for query in queries]
# df = pd.DataFrame(data)
# df.to_json("./tmp_query_category.json", orient="records", force_ascii=False)

DEFAULT_TEXT_QA_PROMPT_TMPL = (
    "Context information is below.\n"
    "---------------------\n"
    "{context}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\n"
    "Query: {query}\n"
    "Answer: "
)

# llm_model_name_or_path = "mistralai/Mistral-7B-Instruct-v0.2"
llm_model_name_or_path = "mistralai/Mixtral-8x7B-Instruct-v0.1"
# llm_model_name_or_path = "microsoft/phi-2"

query_wrapper_prompt = "<s>[INST] {query} [/INST]"
# query_wrapper_prompt = "Instruct: {query}\nOutput: "

model = HuggingFaceLLM(
    model_name=llm_model_name_or_path,
    # device_map="auto",
    device_map="sequential",
    # uncomment this if using CUDA to reduce memory usage
    model_kwargs={
        "torch_dtype": torch.float16,
        "max_memory": {0: '40GiB', 1: '40GiB', 2: '40GiB'},
    },
    tokenizer_kwargs={"max_length": 32768},
    generate_kwargs={"max_new_tokens": 256, "temperature": 0, "do_sample": False, "prompt_lookup_num_tokens": 10},
    query_wrapper_prompt=query_wrapper_prompt,
)

context = "\n\n".join([doc.text for doc in docs_])
context_query = DEFAULT_TEXT_QA_PROMPT_TMPL.format(context=context, query=query)

r = model._predict(context_query)
print(r)
