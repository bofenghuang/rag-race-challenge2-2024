platform: Facebook
topic: Graph-API
subtopic: Insights Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Insights Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/insights


### Metrics

Metric names indicate whether a metric is for a Page or a Page post.

| Suffix | Description |
| --- | --- |
| `_unique` | Indicates that the metric shows the number of unique users who performed a specific action, for example `page_impressions_unique`. **Metrics generated with the `_unique` suffix are approximate and may not be 100% accurate.** |
| `_login` | Indicates whether a person was logged into Facebook, for example, `page_tab_views_login_top`. |
| `_logout` | Indicates whether a person is logged out of Facebook, for example `page_views_logout`. |
| `_source` | Indicates that the metric will be broken down into a list of referral sources, for example `page_fans_by_like_source`. External referrals are broken down by domain. Internal referrals are broken down by Facebook-specific features such as **Profile**, **Search**, **Requests**, **Suggestions**, **Stream**, etc. In these cases the `value` returned will be an object containing a series of key-value pairs where the key is the source name and the value is the metric for that source. |
| `*` | Indicates that a metric is refreshed several times during the day, for example `page_impressions_unique*`. |