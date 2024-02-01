platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search


## Request/response behavior [¶](#request-response-behavior- "Permalink to this headline")

Using the `fromDate` and `toDate` parameters, you can request any time period that the API supports. The 30-Day search API provides Tweets from the most recent 31 days (even though referred to as the '30-Day' API, it makes 31 days available to enable users to make complete-month requests). The Full-Archive search API provides Tweets back to the very first tweet (March 21, 2006). However, a single response will be limited to the lesser of your specified 'maxResults' or 31 days. If matching data or your time range exceeds your specified maxResults or 31 days, you will receive a 'next' token which you should use to paginate through the remainder of your specified time range.

For example, say you are using Full-Archive search and want all Tweets matching your query from January 1, 2017 to June 30, 2017. You will specify that full six-month time period in your request using the `fromDate` and `toDate` parameters. The search API will respond with the first 'page' of Tweets, with the number of Tweets matching your `maxResults` parameter (which defaults to 100). Assuming there are more Tweets (and there most likely will be more), the API will also provide a 'next' token that enables you to make a request for the next 'page' of data. This process is repeated until the API does not return a 'next' token. See the next section for more details.