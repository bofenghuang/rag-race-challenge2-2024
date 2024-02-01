platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search

## Pagination [¶](#pagination- "Permalink to this headline")

When making both data and count requests it is likely that there is more data than can be returned in a single response. When that is the case the response will include a ‘next’ token. The ‘next’ token is provided as a root-level JSON attribute. Whenever a ‘next’ token is provided, there is additional data to retrieve so you will need to keep making API requests.

**Note:** The ‘next’ token behavior differs slightly for data and counts requests, and both are described below with example responses provided in the API Reference section.