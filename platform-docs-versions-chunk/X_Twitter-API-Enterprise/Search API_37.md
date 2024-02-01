platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search

### POST /search/:product/:label[¶](#post-search-product-label "Permalink to this headline")

#### Endpoint pattern:

This endpoint returns data for the specified query and time period. If a time period is not specified the time parameters will default to the last 30 days. Note: This functionality can also be accomplished using a GET request, instead of a POST, by encoding the parameters described below into the URL.