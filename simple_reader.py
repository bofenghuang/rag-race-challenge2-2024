#!/usr/bin/env python
# coding=utf-8

import re
from functools import reduce
from pathlib import Path
import os

from tqdm import tqdm
from llama_index.schema import Document


def get_file_metadata(file_path: str):
    p = Path(file_path)
    dir_name = p.parent.name
    platform_name, topic_name = dir_name.split("_", maxsplit=1)  # todo: catch exception
    subtopic_name = p.stem
    return {
        "platform": platform_name,
        "topic": topic_name,
        "subtopic": subtopic_name,
        "file_path": file_path,
    }


def _normalize_markdown_text(markdown_text: str):
    # normalize header syntax
    # https://www.markdownguide.org/basic-syntax/#alternate-syntax
    markdown_text = re.sub(
        r"^(.*)\n={2,}\n", r"# \1\n", markdown_text, flags=re.MULTILINE
    )
    markdown_text = re.sub(
        r"^(.*)\n-{2,}\n", r"## \1\n", markdown_text, flags=re.MULTILINE
    )
    return markdown_text

class SimplerReader:
    def __init__(self, path):
        self.path = path

    def load_files(self):
        files = [
            os.path.join(dp, f)
            for dp, _, filenames in os.walk(self.path)
            for f in filenames
            if os.path.splitext(f)[1] == ".md"
        ]  # get all files paths

        files = [el for el in files if "README.md" not in el]  # exclude the readme file

        documents = []

        for file in files:
            text = open(file).read()  # read md file
            text_normalized = _normalize_markdown_text(text)
            splits = text_normalized.split("# Resource URL:")
            metadata = get_file_metadata(file)
            for split in splits[1:]:
                url = split.split("\n")[0].strip()
                md_text = "\n".join(split.split("\n")[1:])
                metadata['url'] = url
                documents.append(Document(text=md_text, metadata=metadata))


        platforms = set([el.metadata["platform"] for el in documents])

        documents_per_platforms = {platform: [] for platform in platforms}

        for document in documents:
            documents_per_platforms[document.metadata["platform"]].append(document)

        return documents_per_platforms
