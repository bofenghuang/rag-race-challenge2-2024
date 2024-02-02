#!/bin/bash

# download models / datasets to HF cache

set -x -e

module purge

module load git-lfs
module load unrar
git lfs install

module load anaconda-py3/2023.03
module load cuda/12.1.0
conda activate /gpfswork/rech/eqm/commun/.conda/envs/rag-pipeline

# HF cache
export HF_HOME="$ALL_CCFRWORK/.cache/huggingface"


# git clone https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ $ALL_CCFRWORK/Mixtral-8x7B-Instruct-v0.1-AWQ

# python -c 'from transformers import pipeline; pipe = pipeline("text-generation", model=mistralai/Mixtral-8x7B-Instruct-v0.1")'
python -c 'from transformers import pipeline; pipe = pipeline("text-generation", model="TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ")'
python -c 'from transformers import pipeline; pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")'
python -c 'from sentence_transformers import SentenceTransformer; model = SentenceTransformer("BAAI/bge-m3"))'
