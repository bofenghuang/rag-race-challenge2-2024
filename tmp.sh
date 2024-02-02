# install dependencies
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install -U -qqq llama-index langchain
pip install -U -qqq transformers accelerate datasets autoawq fire

pip install rank-bm25 nltk rake_nltk

pip install -U FlagEmbedding

# download lib data
python -c 'import nltk; nltk.download("stopwords")'


# download models
python -c 'from transformers import AutoProcessor; processor = AutoProcessor.from_pretrained("openai/whisper-large-v3")'


# wandb
wandb offline