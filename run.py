#!/usr/bin/env python
# coding=utf-8
# Copyright 2023  Bofeng Huang

# - chunking 
# - retrieval
# - reranker

import os

os.environ["HF_HOME"] = "/projects/bhuang/.cache/huggingface"
# os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["BITSANDBYTES_NOWELCOME"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

import json
import logging
import sys
from collections import defaultdict
from pathlib import Path

import torch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_index.node_parser import LangchainNodeParser
from llama_index import ServiceContext, SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.indices.struct_store import JSONQueryEngine
from llama_index.llms import HuggingFaceLLM
from llama_index.postprocessor import SentenceTransformerRerank
from llama_index.prompts import PromptTemplate
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.retrievers import BM25Retriever

from reader import NotSimpleDirectoryReader, get_file_metadata
from retriever import NotHardRetriever

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# input_dir = "/home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions"
input_dir = "/home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions-sample"

document_files = defaultdict(list)
for p in Path(input_dir).rglob("*.md"):
    if "README" in p.stem:
        continue
    document_files[p.parent.name.split("_")[0]].append(p.as_posix())
document_names = list(document_files.keys())

documents = {
    doc_name: NotSimpleDirectoryReader(input_files=doc_files, file_metadata=get_file_metadata).load_data()
    for doc_name, doc_files in document_files.items()
}
logging.info(f"Loaded {len([y for x in documents.values() for y in x])} md documents")

# # load documents
# documents = NotSimpleDirectoryReader(
#     input_dir=input_dir,
#     exclude=["README.md"],
#     recursive=True,
#     required_exts=[".md"],
#     # file_extractor
#     file_metadata=get_file_metadata,
# ).load_data()

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

# debug
"""
nodes = text_splitter.get_nodes_from_documents(documents)

nodes_for_df = [{**doc.metadata, "text": doc.get_content("all")} for doc in nodes]
df = pd.DataFrame(nodes_for_df)
# df["length"] = df["text"].map(
#     lambda x: len(tokenizer(x, add_special_tokens=False)["input_ids"])
# )
df["id"] = 1
df["id"] = df.groupby("file_path")["id"].cumsum()
def _get_new_file_path(x):
    s = x["file_path"].replace("platform-docs-versions", "platform-docs-versions-new")
    s_a, s_b = s.rsplit(".", 1)
    return f"{s_a}_{x['id']}.{s_b}"
df["new_file_path"] = df.apply(_get_new_file_path, axis=1)
for row in df.to_dict("records"):
    os.makedirs(os.path.dirname(row["new_file_path"]), exist_ok=True)
    with open(row["new_file_path"], "w") as f:
        f.write(row["text"])
"""

# This will wrap the default prompts that are internal to llama-index
# query_wrapper_prompt = PromptTemplate(
#     "Below is an instruction that describes a task. "
#     "Write a response that appropriately completes the request.\n\n"
#     "### Instruction:\n{query_str}\n\n### Response:"
# )

# load embedding model
# todo: create_and_save_optimum_model
# todo: head+tail
# todo: https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings.html#custom-embedding-model
embed_model_name_or_path = "intfloat/multilingual-e5-large"
embed_model = HuggingFaceEmbedding(
    model_name=embed_model_name_or_path,
    embed_batch_size=32,
    max_length=512,
    pooling="mean",
    normalize=True,
    query_instruction="query:",
    text_instruction="passage:",
)

# load llm
# llm_model_name_or_path = "mistralai/Mistral-7B-Instruct-v0.2"
# llm_model_name_or_path = "mistralai/Mixtral-8x7B-Instruct-v0.1"
llm_model_name_or_path = "microsoft/phi-2"

# query_wrapper_prompt = PromptTemplate("<s>[INST] {query_str} [/INST]")
query_wrapper_prompt = PromptTemplate("<Instruct: {query_str}\nOutput: ")

llm = HuggingFaceLLM(
    model_name=llm_model_name_or_path,
    is_chat_model=True,
    device_map="auto",
    # uncomment this if using CUDA to reduce memory usage
    model_kwargs={"torch_dtype": torch.float16},
    # system_prompt=system_prompt,
    query_wrapper_prompt=query_wrapper_prompt,
    # messages_to_prompt=,
    context_window=32768,
    max_new_tokens=1024,
    generate_kwargs={"temperature": 0, "do_sample": False},
    # stopping_ids=[50278, 50279, 50277, 1, 0],
    tokenizer_name=llm_model_name_or_path,
    tokenizer_kwargs={"max_length": 32768},
    # tokenizer_outputs_to_remove=["token_type_ids"],
)

# todo: vllm, vllm server

# todo: set_global_service_context(service_context)
# transformations = [
#     TokenTextSplitter(chunk_size=512, chunk_overlap=128),
#     TitleExtractor(nodes=5),
#     QuestionsAnsweredExtractor(questions=3),
# ]

service_context = ServiceContext.from_defaults(
    # chunk_size=512,
    transformations=[text_splitter],  # title_extractor, qa_extractor],
    embed_model=embed_model,
    llm=llm,
)

indices = {}
for doc_name_, doc_ in documents.items():
    index_ = VectorStoreIndex.from_documents(
        doc_,
        service_context=service_context,
        # storage_context=storage_context,
        show_progress=True,
    )
    index_.as_retriever(similarity_top_k=5)
    indices[doc_name_] = index_


retriever = NotHardRetriever(indices)


nodes = retriever.retrieve(
    # "What is the impact of climate change on the ocean?"
    "How is content moderation carried out on X?"
)
# ---

# initialize storage context (by default it's in-memory)
storage_context = StorageContext.from_defaults()
storage_context.docstore.add_documents(nodes)

index = VectorStoreIndex.from_documents(documents, service_context=service_context, storage_context=storage_context)

# retireve the top 10 most similar nodes using embeddings
vector_retriever = index.as_retriever(similarity_top_k=10)

# retireve the top 10 most similar nodes using bm25
bm25_retriever = BM25Retriever.from_defaults(nodes=nodes, similarity_top_k=10)

# load rerank model
reranker = SentenceTransformerRerank(top_n=4, model="BAAI/bge-reranker-base")

# query_engine = RetrieverQueryEngine.from_args(
#     retriever=hybrid_retriever,
#     node_postprocessors=[reranker],
#     service_context=service_context,
# )

# response = query_engine.query(
#     "What is the impact of climate change on the ocean?"
# )
