platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/live_media

### Query String Parameters

| Key | Value |
| --- | --- |
| `access_token`  <br>**Required**  <br>_String_ | App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `fields`  <br>_Comma-separated list_ | Comma-separated list of IG Media [fields](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) you want returned for each live IG Media in the result set. |
| `since`  <br>_timestamp_ | A Unix timestamp or `strtotime` data value that points to the start of a range of time-based data. See [time-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#time). |
| `until`  <br>_timestamp_ | A Unix timestamp or `strtotime` data value that points to the end of a range of time-based data. See [time-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#time). |