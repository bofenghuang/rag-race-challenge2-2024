platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/pagination

### Use cases for pagination

**To retrieve all results for a request:** Pagination should most often be used to receive all relevant data related to a specific request and parameters. Pagination is required in cases where there are more matching results than the max\_results for a request. Integrating pagination token data into looping requests will allow you to retrieve all results. Once a response is returned without a next\_token value, it can be assumed that all results have been paged through. Pagination should not be used for polling purposes. To get the most recent results since a previous request, review polling with since\_id.

**To traverse through the results of a request:** Pagination provides directional options for navigating through results from a request, using next\_token and previous\_token values from responses. These tokens can be set as the pagination\_token in the following request, to go to the next or the previous page of results.