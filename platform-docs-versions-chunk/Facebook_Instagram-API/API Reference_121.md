platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/content_publishing_limit

### Fields

| Field | Value Description |
| --- | --- |
| `config`  <br>_Object_ | Returns these values:<br><br>* `quota_total` — The maximum number of [IG Containers](https://developers.facebook.com/docs/instagram-api/reference/ig-container) the app user can publish within the `quota_duration` time period (currently `50`).<br>* `quota_duration` — The period of time in seconds against which the `quota_total` is calculated (currently `86400` seconds, or 24 hours). |
| `quota_usage`  <br>_Comma-separated list_ | The number of times the app user has published an [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) since the time specified in the `since` query string parameter. If the `since` parameter is omitted, this value will be the number of times the app user has published a container within the last 24 hours. This field is returned by default if the `fields` query string parameter is omitted from the query. |