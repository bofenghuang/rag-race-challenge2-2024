#!/bin/bash

set -x -e

module purge

module load anaconda-py3/2023.03
module load cuda/12.1.0
conda activate /gpfswork/rech/eqm/commun/.conda/envs/rag-pipeline

python -c 'from transformers import AutoProcessor; processor = AutoProcessor.from_pretrained("openai/whisper-large-v3")'
