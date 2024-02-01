platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish

### Request Syntax

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media\_publish
  ?creation\_id={creation-id}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}`  <br>_String_ | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-user-id}`  <br>**Required**  <br>_String_ | App user's app-scoped user ID. |

### Query String Parameters

| Key | Placeholder | Description |
| --- | --- | --- |
| `access_token`<br><br>Required | `{access-token}` | The app user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) access token. |
| `creation_id`<br><br>Required | `{creation-id}` | The ID of the [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) to be published. |

### Sample Request

POST graph.facebook.com
  /17841405822304914/media\_publish
    ?creation\_id=17889455560051444

### Sample Response

{
  "id": "17920238422030506"
}