platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/upload

### Response

{
  "id": "{id}",
  "file\_offset": {file-offset}
}

Response property values:

* `{id}` — The upload session ID that was queried.
* `{file-offset}` — An integer that indicates the number of bytes that have been successfully uploaded.

Capture the `file_offset` value and repeat [Step 2: Initiate Upload](#step-2--initiate-upload), assigning the value to the corresponding `file_offset` header. This will resume the upload process from the point of interruption.

### Sample Request

curl -X GET \\
 "https://graph.facebook.com/`v19.0`/upload:MTphd...&access\_token=EAAIT..." \\

### Sample Response

{
  "id": "upload:MTphd",
  "file\_offset": 5238
}

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)