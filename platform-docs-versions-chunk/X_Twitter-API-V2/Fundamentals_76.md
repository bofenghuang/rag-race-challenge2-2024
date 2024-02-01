platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/pagination

### Pagination token definitions

next\_token - Opaque string returned within the meta object response on endpoints which support pagination. Indicates that more results are available and can be used as the pagination\_token parameter in the next request to return the next page of results. The last page of results will not have a next\_token present.

previous\_token - Opaque string returned within the meta object response on endpoints which support pagination. Indicates that there is a previous page of results available, and can be set as the pagination\_token parameter in the next request to return the previous page of results.

pagination\_token - Parameter used in pagination requests. Set to the value of next\_token for the next page of results. Set to the value of previous\_token for the previous page of results.