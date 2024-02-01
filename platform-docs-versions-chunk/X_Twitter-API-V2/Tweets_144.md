platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/paginate


### Polling and listening use cases

This section outlines how you can retrieve recent Tweets by polling the recent search endpoint with the since\_id request parameter. 

With polling use cases, "any new Tweets of interest?" queries are made on an on-going, frequent basis. Unlike historical use cases, that base requests on time, polling use cases typically base requests on Tweet IDs.

Central to the polling use pattern is that every new Tweet has a [unique ID](https://developer.twitter.com/en/docs/twitter-ids) that is 'emitted' from the Twitter platform generally in ascending order. If one Tweet has an ID smaller than another, it means it was posted earlier.

The recent search endpoint support navigating the Tweet archive by Tweet ID. Responses from the endpoint include oldest\_id and newest\_id Tweet IDs. In the polling mode, requests are made with the since\_id set to the largest/newest ID received so far. 

For example, say a query for new Tweets about snow is made every five minutes, and the last Tweet we received had a Tweet ID of 10000. When it is time to poll, the request looks like:

https://api.twitter.com/2/tweets/search/recent?query=snow&since\_id=10000

Next, let's say seven Tweets were posted since our last request. Since all of these fit on a single data 'page', there is no next\_token. The response provides the Tweet ID of the most recent (newest) Tweet:

"meta": {
        "newest\_id": "12000",
        "oldest\_id": "10005",
        "result\_count": 7
    }

  
To make the next polling query, this newest\_id value is used to set the next since\_id parameter:

`https://api.twitter.com/2/tweets/search/recent?query=snow&since_id=12000`

When there is more data available, and next tokens are provided, only th newest\_id value from the first page of results is needed. Each page of data will include newest\_id and oldest\_id values, but the value provided in the first page is the only one needed for the next, regularly scheduled, polling request. So, If you are implementing a polling design, or searching for Tweets by ID range, pagination logic is slightly more complicated. 

Now say that there are now 18 more matching Tweets. The endpoint would respond with this initial response with a full data page and a next\_token for requesting the next page of data from this five minute period. It would also include the newest Tweet ID need for the next polling interval in five minutes.  

"meta": {
        "newest\_id": "13800",
        "oldest\_id": "12500",
        "next\_token": "fnsih9chihsnkjbvkjbsc",
        "result\_count": 10
    }

  
To collect all the matching data for this five minute period, pass the next\_token in your next request, along with the same since\_id value as the previous request.

https://api.twitter.com/2/tweets/search/recent?query=snow&since\_id=12000&next\_token=fnsih9chihsnkjbvkjbsc

"meta": {
        "newest\_id": "12300",
        "oldest\_id": "12010",
        "result\_count": 8
    }

  
This second response provides the remaining eight Tweets, and no next\_token. Note that we do not update our newest\_id value (12300), and instead base our next since\_id request on the first response's newest\_id value:

https://api.twitter.com/2/tweets/search/recent?query=snow&since\_id=13800