platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Tag Existing Media

Use the [IG Media Product Tags](https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags#creating) endpoint to create or update tags on existing [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/).

POST /{ig\-media\-id}/product\_tags

#### Parameters

* `updated_tags` — (**required**) An array of objects specifying which product tags to tag the image or video with (maximum of 5; tags and product IDs must be unique). Each object should have the following information:
* `product_id` — (**required**) Product ID. If the IG Media has not been tagged with this ID the tag will be added to the IG Media. If the media has already been tagged with this ID, the tag's display coordinates will be updated.
* `x` — (images only, **required**) A float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.
* `y` — (images only, **required**) A float that indicates percentage distance from top edge of the published media image. Value must be within `0.0`–`1.0` range.

Tagging media is additive until the 5 tag limit has been reached. If the targeted media has already been tagged by a product in the request, the old tag's `x` and `y` values will be updated with their new values (a new tag will not be added).

Returns `true` if able to update the product, otherwise returns `false`.

#### Sample Request

curl \-i \-X POST \\
 "https://graph.facebook.com/`v19.0`/90010778325754/product\_tags?updated\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3859448974125379'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/v12.0/90010778325754/product\_tags?updated\_tags=\[
  {
    product\_id:'3859448974125379',
    x: 0.5,
    y: 0.8
  }
\]&access\_token=EAAOc...

#### Sample Response

{
  "success": true
}

[](#)