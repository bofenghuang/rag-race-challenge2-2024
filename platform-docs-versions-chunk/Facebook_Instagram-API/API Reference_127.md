platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights


### Query String Parameters

| Parameter | Value |
| --- | --- |
| `{access-token}`  <br>**Required**  <br>_String_ | The app user's User Access Token. |
| `{metric}`  <br>**Required**  <br>_Comma-separated list_ | A comma-separated list of [Metrics](#metrics-and-periods) you want returned. If requesting multiple metrics, they must all have the same compatible [Period](#metrics-and-periods). |
| `{period}`  <br>**Required**  <br>_String_ | A [Period](#metrics-and-periods) that is compatible with the metrics you are requesting. |
| `{since}`  <br>_Unix timestamp_ | Used in conjunction with `{until}` to define a [Range](#range). If you omit `since` and `until`, the API defaults to a 2 day range: yesterday through today.<br><br>  <br><br>**Note**: The pagination cursors (`previous` and `next`) fetch the next time window of results, not the next batch of results within the current time window. |
| `{until}`  <br>_Unix timestamp_ | Used in conjunction with `{since}` to define a [Range](#range). If you omit `since` and `until`, the API defaults to a 2 day range: yesterday through today.<br><br>  <br><br>**Note**: The pagination cursors (`previous` and `next`) fetch the next time window of results, not the next batch of results within the current time window. |