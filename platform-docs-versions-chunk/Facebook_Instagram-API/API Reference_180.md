platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_media

### Request Syntax

GET https://graph.facebook.com/`v19.0`/{ig-user-id}
  ?fields=mentioned\_media.media\_id({media-id}){{fields}}
  &access\_token={access-token}

### Query String Parameters

| Parameter | Value |
| --- | --- |
| `{access_token}`  <br>**Required**  <br>_String_ | The app user's User Access Token. |
| `{fields}`  <br>_Comma-separated list_ | A comma-separated list of IG Media [Fields](#fields) you want returned. If omitted, default Fields will be returned. |
| `{media-id}`  <br>**Required**  <br>_String_ | The ID of the IG Media in which the IG User has been @mentioned in a caption. The ID is included in the [Webhook notification](https://developers.facebook.com/docs/instagram-api/guides/webhooks#reply-comment-mention) payload. |