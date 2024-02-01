platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Appeal Product Rejection

Use the [IG User Product Appeal](https://developers.facebook.com/docs/instagram-api/reference/ig-user/product_appeal#creating) endpoint it you want to provide a way for your app users to appeal product [rejections](https://www.facebook.com/help/instagram/1907693709488725) (tags of rejected products will not appear on published posts). Although not required, we do recommend that you provide a way for app users to appeal rejections, or advise them to appeal rejections [using the Business Manager](https://www.facebook.com/business/help/494867298080532).

POST /{ig\-user\-id}/product\_appeal

#### Parameters

* `appeal_reason` — (**required**) Explanation of why the product should be approved.
* `product_id` — (**required**) Product ID.

Returns `true` if we are able to receive your request, otherwise returns `false`. Response does not indicate appeal outcome.

#### Sample Request

curl \-i \-X POST \\

"https://graph.facebook.com/`v19.0`/90010177253934/product\_appeal?appeal\_reason=product%20is%20a%20toy%20and%20not%20a%20real%20weapon&product\_id=4382881195057752&access\_token=EAAOc..."

#### Sample Response

{
  "success": true
}

[](#)