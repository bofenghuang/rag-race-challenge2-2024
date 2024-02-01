platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Facebook Stability Throttle Codes

  

| Error Code | Description |
| --- | --- |
| `throttled` | Whether the query is throttled or not. Values: `True`, `False` |
| `backend_qps` | First throttling factor `backend_qps`. Supported values:<br><br>* `actual_score`—Actual `backend_qps` of this app. Value: `8`<br>* `limit`—`backend_qps` limit of this app. Value: `5`<br>* `more_info`—Queries need a large number of backend requests to handle. We suggest to send fewer queries or simplify queries with narrower time ranges, fewer object IDs, and so on. |
| `complexity_score` | Second throttling factor `complexity_score`. Supported values:<br><br>* `actual_score`—Actual `complexity_score` of this app. Value: `0.1`<br>* `limit`—`complexity_score` limit of this app. Value: `0.01`<br>* `more_info`—High `complexity_score` means your queries are very complex and request large amounts of data. We suggest to simplify queries with shorter time ranges, fewer object IDs, metrics or breakdowns, and so on. Split large, complex queries into multiple smaller queries and space them out. |