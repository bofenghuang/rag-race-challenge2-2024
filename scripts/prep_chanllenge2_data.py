#!/usr/bin/env python
# coding=utf-8

import json
import os
from pathlib import Path

import pandas as pd

input_dir = "./challenge-2-dataset-and-documentation/dataset/train_cleaned"
output_jsonl_file = "./data/train_sample.jsonl"

input_csv_file = f"{input_dir}/input/questions.csv"
source_dir = f"{input_dir}/output/sources"
answer_dir = f"{input_dir}/output/answers"

df = pd.read_csv(input_csv_file, sep=";")
df["id"] = df["id"].map(lambda x: f"{x:03d}")
print(df.head())

sources = {}
for p in Path(source_dir).glob("*.txt"):
    with open(p.as_posix()) as f:
        sources[p.stem] = f.read().strip()
# print(sources)

answers = {}
for p in Path(answer_dir).glob("*.txt"):
    with open(p.as_posix()) as f:
        answers[p.stem] = f.read().strip()
# print(answers)

df_b = pd.DataFrame({"source": sources, "answer": answers})
df_b = df_b.reset_index().rename(columns={"index": "id"})
print(df_b.head())

df = pd.merge(df, df_b, on="id")
print(df.head())

os.makedirs(os.path.dirname(output_jsonl_file), exist_ok=True)
# df.to_json(output_jsonl_file, orient="records", lines=True, force_ascii=False)
with open(output_jsonl_file, "w") as f:
    for row in df.to_dict("records"):
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
