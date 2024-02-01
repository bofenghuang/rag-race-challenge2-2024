platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search


### Data pagination[¶](#data-pagination "Permalink to this headline")

Requests for data will likely generate more data than can be returned in a single response. Each data request includes a parameter that sets the maximum number of Tweets to return per request. This `maxResults` parameter defaults to 100 and can be set to a range of 10-500. If your query matches more Tweets than the 'maxResults' parameter used in the request, the response will include a 'next' token (as a root-level JSON attribute). This 'next' token is used in the subsequent request to retrieve the next portion of the matching Tweets for that query (i.e. the next 'page”). Next tokens will continue to be provided until you have reached the last 'page' of results for that query when no 'next' token is provided.

To request the next 'page' of data, you must make the exact same query as the original, including `query`, `toDate`, and `fromDate` parameters, if used, and also include a 'next' request parameter set to the value from the previous response. This can be utilized with either a GET or POST request. However, the 'next' parameter must be URL encoded in the case of a GET request.

You can continue to pass in the 'next' element from your previous query until you have received all Tweets from the time period covered by your query. When you receive a response that does not include a 'next' element, it means that you have reached the last page and no additional data is available for the specified query and time range.