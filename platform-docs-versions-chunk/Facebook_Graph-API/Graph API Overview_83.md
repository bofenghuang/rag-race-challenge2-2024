platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/batch-requests

## Errors

Its possible that one of your requested operations may throw an error. This could be because, for example, you don't have permission to perform the requested operation. The response is similiar to the standard Graph API, but encapsulated in the batch response syntax:

\[
    { "code": 403,
      "headers": \[
          {"name":"WWW-Authenticate", "value":"OAuth…"},
          {"name":"Content-Type", "value":"text/javascript; charset=UTF-8"} \],
      "body": "{\\"error\\":{\\"type\\":\\"OAuthException\\", … }}"
    }
\]

Other requests within the batch should still complete successfully and will be returned, as normal, with a `200` status code.