platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/content_publishing_limit

### Sample Request

curl -X GET \\
  'https://graph.facebook.com/`v19.0`/17841405822304914/content\_publishing\_limit?fields=quota\_usage,rate\_limit\_settings&since=1609969714&access\_token=IGQVJ...'

### Sample Response

{
  "data": \[
    {
      "quota\_usage": 2,
      "config": {
        "quota\_total": 50,
        "quota\_duration": 86400
      }
    }
  \]
}

## Updating

This operation is not supported.

## Deleting

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)