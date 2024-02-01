platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media

### Image Story Containers

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
  ?image\_url={image-url}
  &media\_type=STORIES
  &access\_token={access-token}

### Video Story Containers

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
  ?video\_url={video-url}
  &media\_type=STORIES
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-user-id}`  <br>Required | App user's app-scoped user ID. |