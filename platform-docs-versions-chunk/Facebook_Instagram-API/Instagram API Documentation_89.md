platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Get Appeal Status

Use the [IG User Product Appeal](https://developers.facebook.com/docs/instagram-api/reference/ig-user/product_appeal#reading) endpoint to get the status of an appeal for a given [rejected](https://www.facebook.com/help/instagram/1907693709488725) product:

GET /{ig\-user\-id}/product\_appeal

#### Parameters

* `product_id` — (**required**) Product ID.

Returns appeal status metadata. Responses can include the following appeal fields:

* `eligible_for_appeal` — Indicates if decision can be appealed (yes if `true`, no if `false`).
* `product_id` — Product ID.
* `review_status` — Review status. Value can be:
* `approved` — Product is approved.
* `rejected` — Product was rejected.
* `pending` — Still undergoing review.
* `outdated` — Product was approved but has been edited and requires reapproval.
* `""` — No review status.
* `no_review` — No review status.

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/`v19.0`/90010177253934/product\_appeal?product\_id=4029274203846188&access\_token=EAAOc..."

#### Sample Response

{
  "data": \[
    {
      "product\_id": 4029274203846188,
      "review\_status": "approved",
      "eligible\_for\_appeal": false
    }
  \]
}

[](#)