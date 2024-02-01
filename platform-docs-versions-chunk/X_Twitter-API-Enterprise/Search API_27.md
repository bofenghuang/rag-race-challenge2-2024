platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/faq

### Error troubleshooting guide

**Code 404 - Not Found**

1. Please ensure you are using the right parameters for each endpoint (e.g. the `buckets`field can only be used with the counts endpoint, not the data endpoint)
2. Please double check the `:product` `:account_name` and `:label` fields are correct. You can find your `:label` field in the GNIP Console (enterprise customers only).

l