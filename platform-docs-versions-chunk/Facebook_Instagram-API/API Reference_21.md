platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-container

### Request Syntax

GET https://graph.facebook.com/{instagram-container-id}
  ?fields={fields}
  &access\_token={access-token}

### Query String Parameters

| Parameter | Value |
| --- | --- |
| `access_token`  <br>**Required**  <br>_String_ | The app user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `fields`  <br>_Comma-separated list_ | A comma-separated list of [fields](#fields) and [edges](#edges) you want returned. If omitted, default fields will be returned. |