platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-media-id}
  ?fields={fields}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-media-id}` | **Required.** IG Media ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [user access token](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens). |
| `fields` | `{fields}` | Comma-separated list of [fields](#fields) you want returned. |