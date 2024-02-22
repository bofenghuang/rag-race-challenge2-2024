#!/usr/bin/env python
# coding=utf-8

import logging
import os
import sys

import pandas as pd
import torch

from tqdm import tqdm

from category_retriever import ModerateBM25CategoryRetriever
from embed_retriever import BGEM3EmbedDocumentRetriever, BGEM3EmbedModel
from hf_llm import HuggingFaceLLM
from reranker import Reranker
from simple_reader import SimplerReader

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


logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", stream=sys.stdout, level=logging.INFO)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


def main(
    input_csv_file: str,
    input_document_dir: str,
    output_dir: str,
    embed_model_name_or_path: str = "BAAI/bge-m3",
    reranker_model_name_or_path: str = "mistralai/Mistral-7B-Instruct-v0.2",
    # llm_model_name_or_path: str = "mistralai/Mixtral-8x7B-Instruct-v0.1",
    llm_model_name_or_path: str = "TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ",
):
    # 1. load and preprocess documents and queries
    # 1.1. load and preprocess documents to hierarchical chunks
    all_documents, parent_relationships = SimplerReader(input_document_dir).load_files()
    # index and retrieve using the smallest chunks
    documents = all_documents[0]
    # document categories (platforms)
    document_names = list(set([doc.metadata["platform"] for doc in documents]))

    # 1.2. load queries
    df = pd.read_csv(input_csv_file, sep=";")
    query_inputs = df.to_dict("records")
    logging.info(f"Loaded {len(query_inputs)} queries")

    # 2. load retriever utilities
    # 2.1 load category retriever
    category_document_retriever = ModerateBM25CategoryRetriever(
        document_names,
        name_mapping={"x": "x twitter tweet", "booking.com": "booking", "facebook": "facebook meta"},  # todo
        top_k=2,  # todo: hyperparam
    )

    # 2.2.1 load embedding model (dense vector + sparse vector + colbert vector)
    # Setting use_fp16 to True speeds up computation with a slight performance degradation
    embed_model = BGEM3EmbedModel(embed_model_name_or_path, use_fp16=True, device=1)
    # 2.2.2 load embedding retriever
    embed_document_retriever = BGEM3EmbedDocumentRetriever(
        embed_model,
        batch_size=4,  # todo: hyperparam
        # batch_size=12,
        max_query_length=512,  # todo: hyperparam
        max_document_length=512,  # todo: hyperparam
        # score_name="dense_score",
        # score_name = "sparse_dense_score",
        score_name="colbert_sparse_dense_score",
        # weights_for_different_modes = None,  # todo: hyperparam
        top_k=5,
    )

    # 2.3 load reranker
    # actually use a LLM filter here
    # other options: bge-rereanker, rankzephyr
    reranker = Reranker(
        reranker_model_name_or_path,
        model_kwargs={
            "torch_dtype": torch.float16,
            # "use_flash_attention_2": True,
            "low_cpu_mem_usage": True,
        },
        device=1,
    )

    # 2.4 load llm
    # llm_model_name_or_path = "mistralai/Mistral-7B-Instruct-v0.2"
    # llm_model_name_or_path = "microsoft/phi-2"
    query_wrapper_prompt = "<s>[INST] {query} [/INST]"
    # query_wrapper_prompt = "Instruct: {query}\nOutput: "
    model = HuggingFaceLLM(
        model_name=llm_model_name_or_path,
        # device_map="auto",
        # device_map="sequential",
        device_map="cuda:0",
        # uncomment this if using CUDA to reduce memory usage
        model_kwargs={
            "torch_dtype": torch.float16,
            # "max_memory": {0: "60GiB", 1: "40GiB"},
            # "use_flash_attention_2": True,
            "low_cpu_mem_usage": True,
        },
        tokenizer_kwargs={"max_length": 32768},
        generate_kwargs={"max_new_tokens": 1024, "temperature": 0.7, "do_sample": True, "prompt_lookup_num_tokens": 10},
        query_wrapper_prompt=query_wrapper_prompt,
    )

    # 3. indexing
    # todo: generate more metadata (summary, question) to compute embedding
    documents = embed_document_retriever.embed_documents(documents)

    # 4. query

    # small-to-big chunks
    def _small_2_big(docs, n=3):
        new_docs = []
        for doc in docs:
            id_ = doc.id_
            for _ in range(n):
                id_ = parent_relationships[id_]
            new_doc = [doc for doc in all_documents[n] if doc.id_ == id_][0]
            if new_doc.id_ not in [doc.id_ for doc in new_docs]:
                new_docs.append(new_doc)
        logging.info(f"Aggregated from {len(docs)} chunks to {len(new_docs)} bigger chunks")
        return new_docs

    for query_input in tqdm(query_inputs):
        query = query_input["question"]
        # todo: rewrite queries, reciprocal rank fusion
        # query = "How is content moderation carried out on X?"
        # query = "How is content moderation carried out on twitter?"
        # query = "I have access to a set of tweets URLs that I consider to be hateful. How can I use Twitter's API to monitor the average duration between the tweet's creation and its moderation?"
        # 4.0 hierarchical hybird retrieval
        # 4.1 retrieve categories (e.g., linkedin, x)
        documents_, _ = category_document_retriever(query, documents)
        # 4.2 retrieve small chunks
        # todo: hyde
        documents_ = embed_document_retriever(query, documents_)
        # todo: switch order
        # 4.4 rerank chunks
        documents_ = reranker(query, documents_)
        # 4.3 retrieve bigger parent chunks (moussa: turtles)
        documents_ = _small_2_big(documents_, n=3)

        # save ressource url
        query_input["resources"] = list(set([doc.metadata["url"] for doc in documents_]))

        # debug
        # data = [{"query": query, "catgory": category_document_retriever(query, docs)[1]} for query in queries]
        # df = pd.DataFrame(data)
        # df.to_json("./tmp_query_category.json", orient="records", force_ascii=False)

        # 4.5 infer w/ llm
        # todo: few-shot
        # todo: prompt-engineering / fine-tuning for "I don't know" ability
        # todo: strategies: compact, refine
        context = "\n\n".join([doc.text for doc in documents_])
        context_query = DEFAULT_TEXT_QA_PROMPT_TMPL.format(context=context, query=query)
        query_input["prompt"] = context_query
        query_input["response"] = model._predict(context_query)

    # export results
    for query_input in query_inputs:
        dir_ = f"{output_dir}/prompts"
        os.makedirs(dir_, exist_ok=True)
        with open(f"{dir_}/{query_input['id']}.txt", "w") as f:
            f.write(query_input["prompt"])

        dir_ = f"{output_dir}/sources"
        os.makedirs(dir_, exist_ok=True)
        with open(f"{dir_}/{query_input['id']}.txt", "w") as f:
            f.write("\n".join(query_input["resources"]))

        dir_ = f"{output_dir}/answers"
        os.makedirs(dir_, exist_ok=True)
        with open(f"{dir_}/{query_input['id']}.txt", "w") as f:
            f.write(query_input["response"])


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('--input-csv-file', help='Description for foo argument', required=True)
    parser.add_argument('--input-document-dir', help='Description for bar argument', required=True)
    parser.add_argument('--output-dir', help='Description for bar argument', required=True)
    parser.add_argument('--embed-model-name-or-path', help='Description for bar argument', required=True)
    parser.add_argument('--reranker-model-name-or-path', help='Description for bar argument', required=True)
    parser.add_argument('--llm-model-name-or-path', help='Description for bar argument', required=True)
    args = parser.parse_args()

    main(
        input_csv_file=args.input_csv_file,
        input_document_dir=args.input_document_dir,
        output_dir=args.output_dir,
        embed_model_name_or_path=args.embed_model_name_or_path,
        reranker_model_name_or_path=args.reranker_model_name_or_path,
        llm_model_name_or_path=args.llm_model_name_or_path,
    )
