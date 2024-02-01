platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/upload

# Resumable Upload API

The Resumable Upload API allows you to upload large files to the Graph API and resume interrupted upload sessions without having to start over. Once uploaded, you can use an uploaded file's handle with other Graph API endpoints that support them.

Note that the Resumable Upload API is not the only way to upload files. Many nodes have an edge that supports uploading, but most do not have a way to handle large files or a way to resume an interrupted upload session.

References for endpoints that support uploaded file handles will indicate if the endpoints support handles returned by the Resumable Upload API.