platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-media-id}/insights
  ?metric={metric}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-media-id}` | **Required.** IG Media ID. |

### Query String Parameters

| Parameter | Value |
| --- | --- |
| `{access-token}`<br><br>Type: string | **Required**. App user's [User access token](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens). |
| `{metric}`<br><br>Type: Comma-separated list | **Required**. Comma-separated list of [Metrics](#metrics) you want returned. |