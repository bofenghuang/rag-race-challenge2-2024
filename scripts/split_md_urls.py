import pandas as pd
import os

path = "./platform-docs-versions/"
files = [
    os.path.join(dp, f)
    for dp, _, filenames in os.walk(path)
    for f in filenames
    if os.path.splitext(f)[1] == ".md"
]
files = [el for el in files if "README.md" not in el]

docs, urls, texts = [], [], []
count = 0
for file in files:
    text = open(file).read()
    if "Resource URL:" in text:
        splits = text.split("# Resource URL:")
        for split in splits[1:]:
            url = split.split("\n")[0].strip()
            md_text = "\n".join(split.split("\n")[1:])
            docs.append(file)
            urls.append(url)
            texts.append(md_text)

df = pd.DataFrame({"doc": docs, "url": urls, "md_text": texts})

df.to_json("data/docs_per_url.jsonl", lines=True, orient="records", force_ascii=False)
