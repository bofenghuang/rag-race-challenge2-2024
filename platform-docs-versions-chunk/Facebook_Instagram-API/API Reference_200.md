platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/tags

### Request Syntax

GET https://graph.facebook.com/{ig-user-id}/tags
  ?fields={fields}
  &access\_token={access-token}

### Query String Parameters

Include the following query string parameters to augment the request.

| Key | Value |
| --- | --- |
| `access_token`  <br>**Required**  <br>_String_ | The app user's [Instagram User Access Token](https://developers.facebook.com/docs/instagram-basic-display-api/overview#instagram-user-access-tokens). |
| `fields`  <br>_Comma-separated list_ | A comma-separated list of [Fields](#fields) and [Edges](#edges) you want included in the response. If omitted, default fields will be returned. |