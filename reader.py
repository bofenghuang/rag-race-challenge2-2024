#!/usr/bin/env python
# coding=utf-8

import logging
import multiprocessing
import re
import warnings
from functools import reduce
from itertools import repeat
from pathlib import Path
from typing import Any, Callable, Dict, Generator, List, Optional, Type

from tqdm import tqdm
from llama_index.readers.base import BaseReader
from llama_index import SimpleDirectoryReader
from llama_index.schema import Document

# from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter


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


def _extract_url(s: str):
    s = s.strip()
    s = re.search(r"(?<=# Resource URL: )\S+$", s).group(0)
    return s


def _split_by_url(markdown_text: str, metadata: Optional[dict] = None):
    metadata = metadata or {}

    split = re.split(r"(# Resource URL: \S+\n)", markdown_text)
    split = [s for s in split if s]
    assert len(split) == 1 or len(split) % 2 == 0

    if len(split) == 1:
        return [({**metadata, "url": "<EMPTY>"}, split[0])]
    else:
        return [({**metadata, "url": _extract_url(split[idx])}, split[idx + 1]) for idx in range(0, len(split), 2)]


class NotSimpleDirectoryReader(SimpleDirectoryReader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # headers_to_split_on = [("#", "header 1"), ("##", "header 2"), ("###", "header 3")]
        # headers_to_split_on = [("#", "header 1"), ("##", "header 2")]
        # self.text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on, strip_headers=True)

        # self.text_splitter = RecursiveCharacterTextSplitter(
        #     separators=[
        #         # First, try to split along Markdown headings (starting with level 2)
        #         # "\n#{1,6} ",
        #         "\n#{1,3} ",
        #         # Note the alternative syntax for headings (below) is not handled here
        #         # Heading level 2
        #         # ---------------
        #         # End of code block
        #         "```\n",
        #         # Horizontal lines
        #         # "\n\\*\\*\\*+\n",
        #         # "\n---+\n",
        #         # "\n___+\n",
        #         # Note that this splitter doesn't handle horizontal lines defined
        #         # by *three or more* of ***, ---, or ___, but this is not handled
        #         "\n" * 4,
        #         # "\n\n",
        #         # "\n",
        #         # " ",
        #         # "",
        #     ],
        #     chunk_size=512,
        #     chunk_overlap=0,
        #     is_separator_regex=True,
        # )

    @classmethod
    def load_file(
        self,
        input_file: Path,
        file_metadata: Callable[[str], Dict],
        file_extractor: Dict[str, BaseReader],
        filename_as_id: bool = False,
        encoding: str = "utf-8",
        errors: str = "ignore",
    ) -> List[Document]:
        """Static method for loading file.

        NOTE: necessarily as a static method for parallel processing.

        Args:
            input_file (Path): _description_
            file_metadata (Callable[[str], Dict]): _description_
            file_extractor (Dict[str, BaseReader]): _description_
            filename_as_id (bool, optional): _description_. Defaults to False.
            encoding (str, optional): _description_. Defaults to "utf-8".
            errors (str, optional): _description_. Defaults to "ignore".

        input_file (Path): File path to read
        file_metadata ([Callable[str, Dict]]): A function that takes
            in a filename and returns a Dict of metadata for the Document.
        file_extractor (Dict[str, BaseReader]): A mapping of file
            extension to a BaseReader class that specifies how to convert that file
            to text.
        filename_as_id (bool): Whether to use the filename as the document id.
        encoding (str): Encoding of the files.
            Default is utf-8.
        errors (str): how encoding and decoding errors are to be handled,
              see https://docs.python.org/3/library/functions.html#open

        Returns:
            List[Document]: loaded documents
        """
        # metadata: Optional[dict] = None
        metadata: Optional[dict] = {}
        # documents: List[Document] = []

        if file_metadata is not None:
            metadata = file_metadata(str(input_file))

        # do standard read
        with open(input_file, errors=errors, encoding=encoding) as f:
            data = f.read()

        # normalize md text
        data = _normalize_markdown_text(data)

        # split by resource url
        splitted_data = _split_by_url(data, metadata)

        # split by header
        # splitted_data = [
        #     ({**metadata_by_url_, **doc_by_url_by_header_.metadata}, doc_by_url_by_header_.page_content)
        #     for metadata_by_url_, data_by_url_ in splitted_data
        #     for doc_by_url_by_header_ in self.text_splitter.split_text(data_by_url_)
        # ]

        # split by markdown markers
        # splitted_data = [
        #     (metadata_by_url_, doc_by_url_by_header_)
        #     for metadata_by_url_, data_by_url_ in splitted_data
        #     for doc_by_url_by_header_ in self.text_splitter.split_text(data_by_url_)
        # ]

        documents = [Document(text=data_, metadata=metadata_) for metadata_, data_ in splitted_data]

        # doc = Document(text=splitted_data_, metadata=metadata_)
        # documents.append(doc)

        # doc = Document(text=data, metadata=metadata or {})
        # if filename_as_id:
        #     doc.id_ = str(input_file)

        # documents.append(doc)

        return documents

    def load_data(self, show_progress: bool = False, num_workers: Optional[int] = None) -> List[Document]:
        """Load data from the input directory.

        Args:
            show_progress (bool): Whether to show tqdm progress bars. Defaults to False.

        Returns:
            List[Document]: A list of documents.
        """
        documents = []

        files_to_process = self.input_files

        if num_workers and num_workers > 1:
            if num_workers > multiprocessing.cpu_count():
                warnings.warn(
                    "Specified num_workers exceed number of CPUs in the system. "
                    "Setting `num_workers` down to the maximum CPU count."
                )
            with multiprocessing.get_context("spawn").Pool(num_workers) as p:
                results = p.starmap(
                    NotSimpleDirectoryReader.load_file,
                    zip(
                        files_to_process,
                        repeat(self.file_metadata),
                        repeat(self.file_extractor),
                        repeat(self.filename_as_id),
                        repeat(self.encoding),
                        repeat(self.errors),
                    ),
                )
                documents = reduce(lambda x, y: x + y, results)

        else:
            if show_progress:
                files_to_process = tqdm(self.input_files, desc="Loading files", unit="file")
            for input_file in files_to_process:
                documents.extend(
                    NotSimpleDirectoryReader.load_file(
                        input_file=input_file,
                        file_metadata=self.file_metadata,
                        file_extractor=self.file_extractor,
                        filename_as_id=self.filename_as_id,
                        encoding=self.encoding,
                        errors=self.errors,
                    )
                )

        return self._exclude_metadata(documents)
