platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging

## Publish a Tagged Media Container

Use the [IG User Media Publish](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish) endpoint to publish the tagged media container. You may publish up to 25 tagged media containers on behalf of an app user within a 24 hour moving period. If you are publishing a carousel, see [Carousels](#carousels). Only products that have a `review_status` of `approved` will appear on published posts. If any of these products are out of stock, their tags will still appear on the published post.

POST /{ig\-user\-id}/media\_publish

#### Parameters

* `creation_id` — (**required**) The carousel container ID.

If the operation is successful the API will return an IG Media ID.

#### Sample Request

curl \-i \-X POST \\
 "https://graph.facebook.com/`v19.0`/90010177253934/media\_publish?creation\_id=17969578066508312&access\_token=EAAOc"

#### Sample Response

{
  "id": "90010778325754"
}

[](#)