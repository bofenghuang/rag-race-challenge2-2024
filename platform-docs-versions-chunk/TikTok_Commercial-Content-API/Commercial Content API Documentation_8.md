platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-ads/


## Body

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| filters | RequestFilters | The filters that will be applied to the query. | See the "Request example" section below | true |
| search\_term | string | The terms to search for in the query. The limit of the string is 50 characters or less.<br><br>If you provide "search\_term", the "advertiser\_business\_ids" filter will be ignored | mobile games | false |
| search\_type | string | The search type (which is case insensitive):<br><br>* "exact\_phrase": Returns results that contain an exact match for the search term. The default search type.<br>* "fuzzy\_phrase": Returns results that contain any or all of the words in the search term in any order. | fuzzy\_phrase | false |
| max\_count | i64 | The maximum number of results returned at once. The default value is 10 and the maximum value is 50. | 20  | false |
| search\_id | string | A search\_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria.<br><br>If you want to start a new search with an updated`search_term` or `filters` value in the request, remove the `search_id` to avoid getting unexpected results. | 20230501124205358FF99E4D6D1294A2A7 | false |