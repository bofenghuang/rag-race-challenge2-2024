platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/upload

## Upload Steps

Uploading a file is a two step process:

1. Use the [Application Uploads](https://developers.facebook.com/docs/graph-api/reference/application/uploads/) endpoint to describe your file and create an upload session.
2. Use the returned upload session ID to initiate the upload process.

If successful, a file handle will be returned which you can then use with other endpoints that support file handles returned by the Resumable Upload API.