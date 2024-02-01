platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags

### Request Syntax

DELETE https://graph.facebook.com/{api-version}/{ig-media-id}/product\_tags
  ?deleted\_tags={deleted-tags}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-media-id}` | **Required.** IG Media ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `deleted_tags` | `{deleted-tags}` | **Required.** An array containing the following information for each product tag to be deleted<br><br>  <br><br>* `merchant_id` — **Required.** Merchant ID.<br>* `product_id` — **Required.** Product ID. |