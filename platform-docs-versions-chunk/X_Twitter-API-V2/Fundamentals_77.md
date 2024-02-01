platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/pagination


### Fundamentals of pagination

* Endpoints which use pagination, will respond to an initial request with the first page of results, and provide a next\_token within the meta object in the JSON response if additional pages of results are available. To receive all results, this process can be repeated until no next\_token is included in the response.

* Results are delivered in reverse-chronological order. This is true within individual pages, as well as across multiple pages:
    * The first Tweet in the first response will be the most recent.
    * The last Tweet in the last response will be the oldest.

* The max\_results request parameter enables you to configure the number of Tweets returned per response page. There will be a default max\_results and a maximum max\_results.
    
* Every pagination implementation will involve parsing tokens from the response payload, which can be used in subsequent requests. See below for more details on how to construct these requests.

* In some circumstances you may get less than the max\_results page of results. Do not rely on the results per page to always equal the max\_results parameter value.
    
* The best ways to successfully use pagination for complete results are by using loop logic within integration code, or by using a [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) that supports Twitter API v2.