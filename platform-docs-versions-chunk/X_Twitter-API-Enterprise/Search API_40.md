platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search

## Counts endpoint  [¶](#counts-endpoint- "Permalink to this headline")

### /search/:stream/counts[¶](#-search-stream-counts "Permalink to this headline")

#### Endpoint pattern:

`/search/fullarchive/accounts/:account_name/:label/counts.json`

This endpoint returns counts (data volumes) data for the specified query. If a time period is not specified the time parameters will default to the last 30 days. Data volumes are returned as a timestamped array on either daily, hourly (default), or by the minute.

**Note:** This functionality can also be accomplished using a GET request, instead of a POST, by encoding the parameters described below into the URL.