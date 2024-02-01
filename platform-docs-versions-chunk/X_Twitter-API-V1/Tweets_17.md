platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/overview


### Rate limits

As part of our effort to reduce the distribution of spam through our APIs, we enforce App-level rate limit on some of our POST endpoints:

* There is a 300 requests per three hours shared App-level rate limit for the POST statuses/update (post a Tweet) and POST statuses/retweet/:id (post a Retweet) endpoints. This means that you can only post either 300 Tweets or Retweets across all of the authorized users of your developer App during a three hour time period. 
* There is a 1,000 requests per 24 hours App-level rate limit for the POST favorites/create/:id endpoint. This means that you can only like 1,000 Tweets across all of the authorized users of your developer App during a 24 hour time period. 

Please note that you must also consider the user-level rate limits for these endpoints, as they limit the number of posted Tweets or liked Tweets a specific authorized user can make over a given time period. 

You can review each endpoints' rate limits via their [API reference page](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference).