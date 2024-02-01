platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search

### Additional notes[¶](#additional-notes "Permalink to this headline")

* When using a fromDate or toDate in a search request, you will only get results from within your time range. When you reach the last group of results within your time range, you will not receive a 'next' token.
* The 'next' element can be used with any maxResults value between 10-500 (with a default value of 100). The maxResults determines how many Tweets are returned in each response, but does not prevent you from eventually getting all results.
* The 'next' element does not expire. Multiple requests using the same 'next' query will receive the same results, regardless of when the request is made.
* When paging through results using the 'next' parameter, you may encounter duplicates at the edges of the query. Your application should be tolerant of these.

## Data endpoint  [¶](#data-endpoint- "Permalink to this headline")