platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search


### Counts pagination[¶](#counts-pagination "Permalink to this headline")

The 'counts' endpoint provides Tweet volumes associated with a query on either a daily, hourly, or per-minute basis. The 'counts' API endpoint will return a timestamped array of counts for a maximum of a 31-day payload of counts. If you request more than 31 days of counts you will be provided a 'next' token. As with the data 'next' tokens, you must make the exact same query as the original and also include a 'next' request parameter set to the value from the previous response.

Beyond requesting more than 31 days of counts, there is another scenario when a 'next' token is provided. For higher volume queries, there is the potential that the generation of counts will take long enough to trigger a response timeout. When this occurs you will receive less than 31 days of counts but will be provided a 'next' token in order to continue making requests for the entire payload of counts. **_Important:_** Timeouts will only issue full "buckets" - so 2.5 days would result in 2 full day "buckets".