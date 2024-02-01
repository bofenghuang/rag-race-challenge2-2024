platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/data-deletion

## What is and is not deleted

The following forms of data are deleted:

* All output cells in notebook files
* All non-notebook files on researchers' persistent storage
* All S3 bucket files including uploads carried out from within the JupyterHub environment, asynchronous query output, and all query results

The following forms of data are _not_ deleted:

* Notebook files (.ipyhb files)
* Notebook input cells (code and markdown)
* Graphics in notebook cells