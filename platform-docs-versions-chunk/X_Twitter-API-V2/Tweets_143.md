platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/paginate


### Retrieving historical data

This section outlines how you can retrieve Tweets from a period of interest (currently limited to the last seven days) using the start\_time and end\_time request parameters. Historical requests are typically one-time requests in support of research and analysis. 

Making requests for a period of data is the default mode of the recent search endpoint. If a search request does not specify a start\_time, end\_time, or since\_id request parameter, the end\_time will default to "now" (actually 30 seconds before the time of query) and the start\_time will default to seven days ago.

The endpoint will respond with the first 'page' of Tweets in reverse-chronological order, starting with the most recent Tweet. The response JSON payload will also include a next\_token if there are additional pages of data. To collect the entire set of matching Tweets, regardless of the number of pages, requests are made until no next\_token is provided.   

For example, here is an initial request for Tweets with the keyword snow from the last week:

https://api.twitter.com/2/tweets/search/recent?query=snow

The response includes the most recent 10 Tweets, along with these "meta" attributes in the JSON response:

"meta": {
        "newest\_id": "1204860593741553664",
        "oldest\_id": "1204860580630278147",
        "next\_token": "b26v89c19zqg8o3fobd8v73egzbdt3qao235oql",
        "result\_count": 10
    }

  
To retrieve the next 10 Tweets, this next\_token is added to the original request. The request would be:

https://api.twitter.com/2/tweets/search/recent?query=snow&next\_token=b26v89c19zqg8o3fobd8v73egzbdt3qao235oql

The process of looking for a next\_token and including it in a subsequent request can be repeated until all (or some number of) Tweets are collected, or until a specified number of requests have been made. If data fidelity (collecting all matches of your query) is key to your use case, a simple "repeat until request.next\_token is null" design will suffice.