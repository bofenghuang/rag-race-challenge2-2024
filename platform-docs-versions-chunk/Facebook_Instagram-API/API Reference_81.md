platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags

### Response

An object indicating success or failure.

{
  "success": {success}
}

#### Response Contents

| Property | Value |
| --- | --- |
| `success` | Returns `true` if able to update the [IG Media's](https://developers.facebook.com/docs/instagram-api/reference/ig-media) product tags, otherwise returns `false`. |

### cURL Example

#### Request

curl -i -X POST \\
 "https://graph.facebook.com/`v19.0`/90010778325754/product\_tags?updated\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3859448974125379'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/`v19.0`/90010778325754/product\_tags?updated\_tags=\[
  {
    product\_id:'3859448974125379',
    x: 0.5,
    y: 0.8
  }
\]&access\_token=EAAOc...

#### Response

{
  "success": true
}