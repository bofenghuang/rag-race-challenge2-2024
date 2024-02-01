platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Get Tags On Media

Use the [IG Media Product Tags](https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags#reading) endpoint to get tags on published media.

GET /{ig\-media\-id}/product\_tags

Returns an array of product tags and their metadata on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/). Responses can include the following product tag fields:

* `product_id` — Product ID.
* `merchant_id` — Merchant ID.
* `name` — Product name.
* `price_string` — Product price.
* `image_url` — Product image URL.
* `review_status` — Indicates product tag eligibility status. Values can be:
* `approved` — Product is approved.
* `rejected` — Product was rejected.
* `pending` — Still undergoing review.
* `outdated` — Product was approved but has been edited and requires reapproval.
* `""` — No review status.
* `no_review` — No review status.
* `is_checkout` — If `true`, product can be purchased directly through the Instagram app. If `false`, product can only be purchased on the merchant's website.
* `stripped_price_string` — Product short price string (price displayed in constrained spaces, such as `$100` instead of `100 USD`).
* `string_sale_price_string` — Product sale price.
* `x` — A float that indicates percentage distance from left edge of media image. Value within `0.0`–`1.0` range.
* `y` — A float that indicates percentage distance from top edge of media image. Value within `0.0`–`1.0` range.

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/`v19.0`/90010778325754/product\_tags?access\_token=EAAOc..."

#### Sample Response

{
  "data": \[
    {
      "product\_id": 3231775643511089,
      "merchant\_id": 90010177253934,
      "name": "Gummy Wombats",
      "price\_string": "$3.50",
      "image\_url": "https://scont...",
      "review\_status": "approved",
      "is\_checkout": true,
      "stripped\_price\_string": "$3.50",
      "x": 0.5,
      "y": 0.80000001192093
    }
  \]
}

[](#)