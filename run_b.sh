#!/bin/bash

set -x -e

module purge

module load anaconda-py3/2023.03
module load cuda/12.1.0
conda activate /gpfswork/rech/eqm/commun/.conda/envs/rag-pipeline

# HF cache
export HF_HOME="$ALL_CCFRWORK/.cache/huggingface"

# models
embed_model_name_or_path="BAAI/bge-m3"
reranker_model_name_or_path="mistralai/Mistral-7B-Instruct-v0.2"
# llm_model_name_or_path="/gpfsdswork/dataset/HuggingFace_Models/TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ"
llm_model_name_or_path="/gpfsdswork/dataset/HuggingFace_Models/mistralai/Mixtral-8x7B-Instruct-v0.1"

# data
input_csv_file="./challenge-2-dataset-and-documentation/dataset/train/input/questions.csv"
input_document_dir="./platform-docs-versions"
output_dir="./outputs"

# python run.py \
#     --input_csv_file $input_csv_file \
#     --input_document_dir $input_document_dir \
#     --output_dir $output_dir \
#     --embed_model_name_or_path $embed_model_name_or_path \
#     --reranker_model_name_or_path $reranker_model_name_or_path \
#     --llm_model_name_or_path $llm_model_name_or_path

python run.py \
    --input-csv-file $input_csv_file \
    --input-document-dir $input_document_dir \
    --output-dir $output_dir \
    --embed-model-name-or-path $embed_model_name_or_path \
    --reranker-model-name-or-path $reranker_model_name_or_path \
    --llm-model-name-or-path $llm_model_name_or_path
