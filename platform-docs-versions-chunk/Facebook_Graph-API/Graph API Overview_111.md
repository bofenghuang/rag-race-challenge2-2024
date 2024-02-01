platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/upload

## Interruptions

If you have initiated an upload session but it is taking longer than expected or has been interrupted, send a `GET` request to Graph API host address and append your upload session ID. The API returns a `file_offset` value that you can use to resume the upload process from the point of interruption.

### Request Syntax

GET https://graph.facebook.com/{api-version}/{upload-session-id}
  ?access\_token={access-token}

Placeholder values:

* `{api-version}` — Graph API version.
* `{upload-session-id}` — Upload session ID returned in [Step 1: Create a Session](#step-1--create-a-session).
* `{access-token}` — App user's User Access Token.