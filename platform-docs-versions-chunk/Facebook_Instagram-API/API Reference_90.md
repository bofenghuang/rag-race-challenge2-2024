platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags

### cURL Example

#### Request

curl -i -X DELETE \\
  "https://graph.facebook.com/`v19.0`/90010778325754/product\_tags?deleted\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3859448974125379'%2C%0A%20%20%20%20merchant\_id%3A'90010177253934'%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/v12.0/90010778325754/product\_tags?deleted\_tags=\[
  {
    product\_id:'3859448974125379',
    merchant\_id:'90010177253934'
  }
\]&access\_token=EAAOc...

#### Response

{
  "success": true
}

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)