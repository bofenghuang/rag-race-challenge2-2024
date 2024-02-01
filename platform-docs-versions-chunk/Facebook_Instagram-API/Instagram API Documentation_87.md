platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Delete Tags

Use the [IG Media Product Tags](https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags#deleting) endpoint to delete tags on a published [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) including Reels.

DELETE /{ig\-media\-id}/product\_tags

#### Parameters

* `deleted_tags` — (**required**) An array containing the following information for each product tag to be deleted:
* `merchant_id` — (**required**) Merchant ID.
* `product_id` — (**required**) Product ID.

Returns `true` if tag deletion successful, otherwise returns `false`.

#### Sample Request

curl \-i \-X DELETE \\
 "https://graph.facebook.com/`v19.0`/90010778325754/product\_tags?deleted\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3859448974125379'%2C%0A%20%20%20%20merchant\_id%3A'90010177253934'%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/v12.0/90010778325754/product\_tags?deleted\_tags=\[
  {
    product\_id:'3859448974125379',
    merchant\_id:'90010177253934'
  }
\]&access\_token=EAAOc...

#### Sample Response

{
  "success": true
}

[](#)