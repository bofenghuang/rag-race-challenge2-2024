platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Catalog

#### Catalog Batch

Requests made by your app are counted against the rate limit metrics such as call count, total CPU time and total time your app can make in a rolling one hour period per each catalog ID and is calculated as follows:

`Calls within one hour = 200 + 200 * log2(unique users)`

The unique users is a number of unique users of the business (on all catalogs) with intent in the last 28 days. The more users see products from your catalogs, the more call quota is allocated.

| Type of Call | Endpoint |
| --- | --- |
| POST | /{catalog\_id}/items\_batch |
| POST | /{catalog\_id}/localized\_items\_batch |
| POST | /{catalog\_id}/batch |

#### Catalog Management

Requests made by your app are counted against the number of calls your app can make in a rolling one hour period per each catalog ID and is calculated as follows:

`Calls within one hour = 20,000 + 20,000 * log2(unique users)`

The unique users is a number of unique users of the business (on all catalogs) with intent in the last 28d. The more users see products from your catalogs, the more call quota is allocated.

This formula is applied on various catalog endpoints.

For more information on how to get your current rate usage, see [Headers](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers).

Rate limiting may also be subject to the total CPU time and total wall time during a rolling one hour window. For more details, check the HTTP [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header `total_cputime` and `total_time`.

If you are receiving rate limiting errors, you can also refer to `estimated_time_to_regain_access` in the [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header for the estimated blocking time.