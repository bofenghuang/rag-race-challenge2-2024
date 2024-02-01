platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/integrate

### Pagination

These endpoints utilize pagination so that responses are returned quickly. In cases where there are more results than what can be sent in a single response (up to 100 events) you will need to paginate. Use the max\_results parameter to identify how many results will return per page, and the pagination\_token parameter to return the next page of results. You can learn more by reviewing our [pagination guide](https://developer.twitter.com/en/docs/twitter-api/pagination).