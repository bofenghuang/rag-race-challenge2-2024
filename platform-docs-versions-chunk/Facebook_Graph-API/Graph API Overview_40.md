platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Ads Management

Requests made by your app to the Ads Management API are counted against the app's rate limit metrics such as call count, total CPU time and total time. An app's call count is the number of calls it can make during a rolling one hour window and is calculated as follows:

For apps with [Standard Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#standard-access)to the Ads Management Standard Access feature:

`Calls within one hour = 300 + 40 * Number of Active ads`

For apps with [Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#advanced-access) to the Ads Management Standard Access feature:

`Calls within one hour = 100000 + 40 * Number of Active ads`

The Number of Active Ads is the number of ads for each ad account.

Rate limiting may also be subject to the total CPU time and total wall time during a rolling one hour window. For more details, check the HTTP [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header `total_cputime` and `total_time`.

If you are receiving rate limiting errors, you can also refer to `estimated_time_to_regain_access` in the [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header for the estimated blocking time.