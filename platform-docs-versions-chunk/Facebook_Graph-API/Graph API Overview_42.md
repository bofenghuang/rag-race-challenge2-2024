platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Custom Audience

Requests made by your app to the Custom Audience API are counted against the app's rate limit metrics such as call count, total CPU time and total time. An app's call count is the number of calls it can make during a rolling one hour window and is calculated as follows but will never exceed 700000:

For apps with [Standard Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#standard-access) to the Ads Management Standard Access feature:

`Calls within one hour = 5000 + 40 * Number of Active Custom Audiences`

For apps with [Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#advanced-access) to the Ads Management Standard Access feature:

`Calls within one hour = 190000 + 40 * Number of Active Custom Audiences`

The Number of Active Custom Audiences is the number of active [custom audiences](https://developers.facebook.com/docs/marketing-api/audiences-api) for each ad account.

Rate limiting may also be subject to the total CPU time and total wall time during a rolling one hour window. For more details, check the HTTP [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header `total_cputime` and `total_time`.

If you are receiving rate limiting errors, you can also refer to `estimated_time_to_regain_access` in the [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header for the estimated blocking time.