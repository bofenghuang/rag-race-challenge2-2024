platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights


### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** The app user's [User](https://developers.facebook.com/docs/facebook-login/guides/access-tokens#usertokens) access token. |
| `breakdown` | `{breakdown}` | Designates how to break down result set into subsets. See [Breakdown](#breakdown). |
| `metric` | `{metric}` | **Required.** Comma-separated list of [Metrics](#metrics) you want returned. |
| `metric_type` | `{metric-type}` | Designates if you want the responses aggregated by time period or as a simple total. See [Metric Type](#metric-type). |
| `period` | `{period}` | **Required.** [Period](#period) aggregation. |
| `since` | `{since}` | Unix timestamp indicating start of range. See [Range](#range-2). |
| `timeframe` | `{timeframe}` | **Required for demographics-related metrics.** Designates how far to look back for data. See [Timeframe](#timeframe). |
| `until` | `{until}` | Unix timestamp indicating end of range. See [Range](#range-2). |