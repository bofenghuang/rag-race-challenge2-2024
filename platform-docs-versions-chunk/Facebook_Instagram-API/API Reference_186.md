platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/product_appeal

### Request Syntax

POST https://graph.facebook.com/{api-version}/{ig-user-id}/product\_appeal
  ?appeal\_reason={appeal-reason}
  &product\_id={product-id}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-user-id}` | **Required.** App user's app-scoped user ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `appeal_reason` | `{appeal-reason}` | **Required.** Explanation of why the product should be approved. |
| `product_id` | `{product-id}` | **Required.** Product ID. |