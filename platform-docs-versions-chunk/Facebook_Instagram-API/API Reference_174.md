platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_comment

### Request Syntax

GET https://graph.facebook.com/`v19.0`/{ig-user-id}
  ?fields=mentioned\_comment.comment\_id({comment-id}){{fields}}
  &access\_token={access-token}

### Query String Parameters

| Parameter | Value |
| --- | --- |
| `{access_token}`  <br>**Required**  <br>_String_ | The app user's User Access Token. |
| `{comment-id}`  <br>**Required**  <br>_String_ | The ID of the IG Comment in which the IG User has been @mentioned. The ID is included in the [Webhook notification](https://developers.facebook.com/docs/instagram-api/guides/webhooks#reply-comment-mention) payload. |
| `{fields}`  <br>_Comma-separated list_ | A comma-separated list of IG Comment [Fields](#fields) you want returned. If omitted, default fields will be returned. |