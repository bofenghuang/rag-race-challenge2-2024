platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Ads Insights

Requests made by your app to the Ads Insights API are counted against the app's rate limit metrics such as call count, total CPU time and total time. An app's call count is the number of calls it can make during a rolling one hour window and is calculated as follows:

For apps with [Standard Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#standard-access) to the Ads Management Standard Access feature:

`Calls within one hour = 600 + 400 * Number of Active ads - 0.001 * User Errors`

For apps with [Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#advanced-access) to the Ads Management Standard Access feature:

`Calls within one hour = 190000 + 400 * Number of Active ads - 0.001 * User Errors`

The Number of Active ads is the number of ads currently running per ad account. User Errors is the number of errors received when calling the API. To get a higher rate limit, you can apply for the [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features) feature.

Rate limiting may also be subject to the total CPU time and total wall time during a rolling one hour window. For more details, check the HTTP [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header `total_cputime` and `total_time`.

If you are receiving rate limiting errors, you can also refer to `estimated_time_to_regain_access` in the [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header for the estimated blocking time.