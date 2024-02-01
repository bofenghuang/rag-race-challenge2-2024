platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/build-standard-query


## How to build a query

Standard

The best way to build a query and test if it’s valid and will return matched Tweets is to first try it at [twitter.com/search](https://twitter.com/search). As you get a satisfactory result set, the URL loaded in the browser will contain the proper query syntax that can be reused in the API endpoint. Here’s an example:

1. We want to search for Tweets referencing @twitterapi account. First, we run the search on [twitter.com/search](https://twitter.com/search)
2. Check and copy the URL loaded. In this case, we got: [https://twitter.com/search?q=%40twitterapi](https://twitter.com/search?q=%40twitterapi)
3. Replace https://twitter.com/search with https://api.twitter.com/1.1/search/tweets.json and you will get: https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi
4. Run a Twurl command to execute the search.

Please note that the API requires that the request is authenticated (check [Authentication & Authorization](https://developer.twitter.com/en/docs/basics/authentication/overview/authentication-and-authorization.html) documentation for more details on this). Also note that the search results at twitter.com may return historical results, while the Search API usually only serves Tweets from the past week.