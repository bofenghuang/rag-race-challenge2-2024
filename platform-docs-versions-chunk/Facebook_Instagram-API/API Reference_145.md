platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/live_media

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-user-id}/live\_media
  ?access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}`  <br>_String_ | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-user-id}`  <br>**Required**  <br>_String_ | App user's app-scoped user ID. |