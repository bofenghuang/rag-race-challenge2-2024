platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags


### Response

A JSON-formatted object containing an array of product tags on an IG Media. Responses can include the following product tag fields:

{
  "data": \[
    {
      "product\_id": {product-id},
      "merchant\_id": {merchant-id},
      "name": "{name}",
      "price\_string": "{price-string}",
      "image\_url": "{image-url}",
      "review\_status": "{review-status}",
      "is\_checkout": {is-checkout},
      "stripped\_price\_string": "{stripped-price-string}",
      "string\_sale\_price\_string": "{string-sale-price-string}",
      "x": {x},
      "y": {y}
    }
  \]
}

#### Response Contents

| Property | Value |
| --- | --- |
| `product_id` | Product ID. |
| `merchant_id` | Merchant ID. |
| `name` | Product name. |
| `price_string` | Price string. |
| `image_url` | Product image URL. |
| `review_status` | Product review status. Values can be:<br><br>  <br><br>* `approved` — Product is approved.<br>* `rejected` — Product was rejected<br>* `pending` — Still undergoing review.<br>* `outdated` — Product was approved but has been edited and requires reapproval.<br>* `""` — No review status. |
| `is_checkout` | If `true`, product can be purchased directly through the Instagram app. If `false`, product can only be purchased on the merchant's website. |
| `stripped_price_string` | Product short price string (price displayed in constrained spaces, such as `$100` instead of `100 USD`). |
| `string_sale_price_string` | Product sale price. |
| `x` | A float that indicates percentage distance from left edge of media image. Value within `0.0`–`1.0` range. |
| `y` | A float that indicates percentage distance from top edge of media image. Value within `0.0`–`1.0` range. |