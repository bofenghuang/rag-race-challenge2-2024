platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-comment

### Edges

| Edge | Description |
| --- | --- |
| [`replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-comment/replies) | Get a list of IG Comments on the IG Comment; Create an IG Comment on an IG Comment. |

### Response

A JSON-formatted object containing default and requested [fields](#fields) and [edges](#edges).

{
  "{field}":"{value}",
  ...
}

### cURL Example

#### Request

curl -i -X GET \\
 "https://graph.facebook.com/`v19.0`/17881770991003328?fields=hidden%2Cmedia%2Ctimestamp&access\_token=EAAOc..."

#### Response

{
  "hidden": false,
  "media": {
    "id": "17856134461174448"
  },
  "timestamp": "2017-05-19T23:27:28+0000",
  "id": "17881770991003328"
}

## Updating