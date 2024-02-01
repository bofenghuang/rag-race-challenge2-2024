#!/usr/bin/env python
# coding=utf-8

import re
from functools import reduce
from pathlib import Path
import os

from tqdm import tqdm
from llama_index.schema import Document


max_tokens = 512  # should be repalced


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


def split_long_chunks(doc):
    new_chunks = []
    text = doc.text
    # let's split first on \n\n to avoid crashing tables.
    splits = text.split("\n\n")
    current_chunk = splits[0]
    metadata = doc.metadata
    metadata["parent"] = doc.id_
    for split in splits[1:]:
        if len((current_chunk + "\n\n" + split).split()) > max_tokens:
            new_chunks.append(Document(text=current_chunk, metadata=metadata))
            current_chunk = split
        else:
            current_chunk = current_chunk + "\n\n" + split
    new_chunks.append(Document(text=current_chunk, metadata=metadata))
    return new_chunks


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
                metadata["url"] = url
                documents.append(Document(text=md_text, metadata=metadata))

        documents_chunks = []
        documents_smaller_chunks = []
        documents_smaller_smaller_chunks = []

        for document in documents:
            text = document.text
            # text = text.replace("\n## ", "\n# ").replace("\n\n\n\n", "\n# ")
            chunks = text.split("\n# ")

            for chunk in chunks:
                if len(chunk.strip()) > 10:
                    metadata = document.metadata
                    metadata["parent"] = document.id_
                    doc = Document(text=chunk, metadata=metadata)
                    documents_chunks.append(doc)

        for document in documents_chunks:
            text = document.text
            smaller_chunks = text.split("\n## ")

            for chunk in smaller_chunks:
                if len(chunk.strip()) > 10:
                    metadata = document.metadata
                    metadata["parent"] = document.id_
                    doc = Document(text=chunk, metadata=metadata)
                    documents_smaller_chunks.append(doc)

        for document in documents_smaller_chunks:
            text = document.text
            smaller_smaller_chunks = text.split("\n### ")

            for chunk in smaller_smaller_chunks:
                if len(chunk.strip()) > 10:
                    metadata = document.metadata
                    metadata["parent"] = document.id_
                    doc = Document(text=chunk, metadata=metadata)
                    documents_smaller_smaller_chunks.append(doc)
        smallest_chunks = []

        for el in documents_smaller_smaller_chunks:
            if len(el.text.split()) > max_tokens:
                smallest_chunks += split_long_chunks(el)
            else:
                smallest_chunks.append(el)
        # platforms = set([el.metadata["platform"] for el in documents])

        # documents_per_platforms = {platform: [] for platform in platforms}

        # for document in documents:
        #     documents_per_platforms[document.metadata["platform"]].append(document)

        # return documents_per_platforms
        return (
            documents,
            documents_chunks,
            documents_smaller_chunks,
            documents_smaller_smaller_chunks,
            smallest_chunks
        )
