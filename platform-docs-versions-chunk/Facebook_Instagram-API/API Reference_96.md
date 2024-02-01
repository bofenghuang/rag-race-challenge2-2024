platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user

### Response

A JSON-formatted object containing default and requested [fields](#fields) and [edges](#edges).

{
  "{field}":"{value}",
  ...
}

### cURL Example

#### Request

curl -X GET \\
  'https://graph.facebook.com/`v19.0`/17841405822304914?fields=biography%2Cid%2Cusername%2Cwebsite&access\_token=EAACwX...'

#### Response

{
  "biography": "Dino data crunching app",
  "id": "17841405822304914",
  "username": "metricsaurus",
  "website": "http://www.metricsaurus.com/"
}

## Updating

This operation is not supported.

## Deleting

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)