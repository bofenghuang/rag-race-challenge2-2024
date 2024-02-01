platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags

### cURL Example

#### Request

curl -i -X GET \\
 "https://graph.facebook.com/`v19.0`/90010778325754/product\_tags?access\_token=EAAOc..."

#### Response

{
  "data": \[
    {
      "product\_id": 3231775643511089,
      "merchant\_id": 90010177253934,
      "name": "Gummy Bears",
      "price\_string": "$3.50",
      "image\_url": "https://scont...",
      "review\_status": "approved",
      "is\_checkout": true,
      "stripped\_price\_string": "$3.50",
      "stripped\_sale\_price\_string": "$3",
      "x": 0.5,
      "y": 0.80000001192093
    }
  \]
}

## Updating

See [Creating](#creating).

## Deleting

**`DELETE /{ig-media-id}/product_tags`**

Delete product tags on an existing [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.