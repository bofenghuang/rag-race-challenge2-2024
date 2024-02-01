platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/catalog_product_search

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-user-id}/catalog\_product\_search
  ?catalog\_id={catalog-id}
  &q={q}
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
| `catalog_id` | `{catalog-id}` | **Required.** ID of catalog to search. |
| `q` | `{q}` | A string to search for in each product's name or SKU number (SKU numbers can be added in the **Content ID** column in the catalog management interface). If no string is specified, all tag-eligible products will be returned. |