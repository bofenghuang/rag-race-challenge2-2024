platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/content_publishing_limit

### Request Syntax

GET https://graph.facebook.com/v9.0/{ig-user-id}/content\_publishing\_limit
  ?fields={fields}
  &since={since}
  &access\_token={access-token}

### Query String Parameters

| Placeholder | Value Description |
| --- | --- |
| `{access-token}`  <br>**Required**  <br>_String_ | The app user's User Access Token. |
| `{fields}`  <br>_Comma-separated list_ | A comma-separated list of [fields](#fields) you want returned. If omitted, the `quota_usage` field will be returned by default. |
| `{since}`  <br>_Unix timestamp_ | A Unix timestamp no older than 24 hours. |