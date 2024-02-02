#!/bin/bash

set -x -e

module purge

module load anaconda-py3/2023.03
module load cuda/12.1.0
conda activate /gpfswork/rech/eqm/commun/.conda/envs/rag-pipeline

python -c 'from transformers import AutoProcessor; processor = AutoProcessor.from_pretrained("openai/whisper-large-v3")'

python -c 'from transformers import pipeline; pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")'
python -c 'from transformers import pipeline; pipe = pipeline("text-generation", model="TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ")'
python -c 'from transformers import pipeline; pipe = pipeline("text-generation", model="TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ")'