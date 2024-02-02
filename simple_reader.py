#!/usr/bin/env python
# coding=utf-8

import os
import re
import uuid
from functools import reduce
from pathlib import Path
from typing import Any, Dict, List, Optional

# from llama_index.schema import Document
from pydantic import BaseModel, Field
from tqdm import tqdm

MAX_TOKENS = 512  # should be replaced


class Document(BaseModel):
    id_: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="Unique ID of the node.",
        # alias="doc_id",
    )

    text: str = Field(default="", description="Text content of the node.")

    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="A flat dictionary of metadata fields",
        # alias="extra_info",
    )

    excluded_embed_metadata_keys: List[str] = Field(
        default_factory=list,
        description="Metadata keys that are excluded from text for the embed model.",
    )
    excluded_llm_metadata_keys: List[str] = Field(
        default_factory=list,
        description="Metadata keys that are excluded from text for the LLM.",
    )

    dense_embedding: Optional[Any] = Field(
        default=None
    )
    sparse_embedding: Optional[Any] = Field(
        default=None
    )
    colbert_embedding: Optional[Any] = Field(
        default=None
    )

    def __setstate__(self, state: Dict[str, Any]) -> None:
        # Use the __dict__ and __init__ method to set state
        # so that all variable initialize
        try:
            self.__init__(**state["__dict__"])  # type: ignore
        except Exception:
            # Fall back to the default __setstate__ method
            super().__setstate__(state)


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
    markdown_text = re.sub(r"^(.*)\n={2,}\n", r"# \1\n", markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r"^(.*)\n-{2,}\n", r"## \1\n", markdown_text, flags=re.MULTILINE)
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
        if len((current_chunk + "\n\n" + split).split()) > MAX_TOKENS:
            new_chunks.append(Document(text=current_chunk, metadata=metadata))
            current_chunk = split
        else:
            current_chunk = current_chunk + "\n\n" + split
    new_chunks.append(Document(text=current_chunk, metadata=metadata))
    return new_chunks


class SimplerReader:
    def __init__(self, path):
        self.path = path
        self.parents_dic = {}

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

        documents_chunks = []  # 1 diese
        documents_smaller_chunks = []  # 2 diese
        documents_smaller_smaller_chunks = []  # 3 diese
        smallest_chunks = []  # split

        for document in documents:
            text = document.text
            # text = text.replace("\n## ", "\n# ").replace("\n\n\n\n", "\n# ")
            chunks = text.split("\n# ")

            for chunk in chunks:
                if len(chunk.strip()) > 10:
                    metadata = document.metadata
                    metadata["parent"] = document.id_
                    doc = Document(text=chunk, metadata=metadata)
                    self.parents_dic[doc.id_] = document
                    documents_chunks.append(doc)

        for document in documents_chunks:
            text = document.text
            smaller_chunks = text.split("\n## ")

            for chunk in smaller_chunks:
                if len(chunk.strip()) > 10:
                    metadata = document.metadata
                    metadata["parent"] = document.id_
                    doc = Document(text=chunk, metadata=metadata)
                    self.parents_dic[doc.id_] = document
                    documents_smaller_chunks.append(doc)

        for document in documents_smaller_chunks:
            text = document.text
            smaller_smaller_chunks = text.split("\n### ")

            for chunk in smaller_smaller_chunks:
                if len(chunk.strip()) > 10:
                    metadata = document.metadata
                    metadata["parent"] = document.id_
                    doc = Document(text=chunk, metadata=metadata)
                    self.parents_dic[doc.id_] = document
                    documents_smaller_smaller_chunks.append(doc)

        for el in documents_smaller_smaller_chunks:
            if len(el.text.split()) > MAX_TOKENS:
                new_splits = split_long_chunks(el)
                for split in new_splits:
                    self.parents_dic[split.id_] = el
                smallest_chunks += new_splits
            else:
                self.parents_dic[doc.id_] = el
                el.metadata['parent'] = el.id_
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
            smallest_chunks,
        )
