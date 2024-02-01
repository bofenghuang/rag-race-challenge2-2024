platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/collaborators

### Request syntax

GET https://graph.facebook.com/{appi-version}/{ig-media-id}/collaborators

### Sample Response

{
  "data": \[
    {
      "id": "90010775360791",
      "username": "realtest1",
      "invite\_status": "Accpeted"
    },
    {
      "id": "17841449208283139",
      "username": "realtest2",
      "invite\_status": "Pending"
    },
    {
      "id": "90011117049518",
      "username": "realtest3",
      "invite\_status": "Declined"
    }
  \]
}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-user-id}` | **Required.** IG User ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |