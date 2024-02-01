platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/paginate


### Introduction

Search queries typically match on more Tweets than can be returned in a single API response. When that happens, the data is returned in a series of 'pages'. Pagination refers to methods for requesting all of the pages in order to retrieve the entire data set.

Here are fundamental recent search pagination details:

* The recent search endpoints will respond to a query with at least one page, and provide a next\_token in its JSON response if additional pages are available. To receive matching Tweets, this process can be repeated until no token is included in the response.
* The next\_token does not expire. Multiple requests using the same next\_token value will receive the same results, regardless of when the request is made.

* Tweets are delivered in reverse-chronological order, in the UTC timezone. This is true within individual pages, as well as across multiple pages: 
    * The first Tweet in the first response will be the most recent one matching your query.
    * The last Tweet in the last response will be the oldest one matching your query.

* The max\_results request parameter enables you to configure the number of Tweets returned per response. This defaults to 10 Tweets and has a maximum of 100. 

* Every pagination implementation will involve parsing next\_tokens from the response payload, and including them in the 'next page' search request. See below for more details on how to construct these 'next page' requests.  
     

The recent search endpoint was designed to support two fundamental use patterns:

* **Get historical** - Requesting matching Tweets from a time period of interest. These are typically one-time requests in support of historical research. Search requests can be based on start\_time and end\_time request parameters. recent search endpoint respond with Tweets delivered in reverse-chronological order, starting with the most recent matching Tweet. 

* **Polling** - Requesting matching Tweets that have been posted since the last Tweet received. These use cases often have a near-real-time focus and are characterized by frequent requests, "listening" for new Tweets of interest. The recent search endpoint provide the since\_id request parameter in support of the 'polling' pattern. To help with navigating by Tweet IDs, the until\_id request parameter is also available.  
     

Next, we'll discuss the historical mode. This is the default mode of the recent search endpoint and illustrates the fundamentals of pagination. Then we'll discuss examples of polling use cases. When polling triggers pagination, there is an additional step to manage search requests.