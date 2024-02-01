platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream


# GET /2/tweets/search/stream

Streams Tweets in real-time that match the rules that you added to the stream using the [POST /tweets/search/stream/rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules) endpoint. If you haven't added any rules to your stream, you will not receive any Tweets.  
  
If you have been approved for [Academic Research access](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level), you can take advantage of the [redundant connections](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/recovery-and-redundancy-features) functionality, which allows you to connect to a stream up to two times, which will help maximize your streaming up-time.  
  
The Tweets returned by this endpoint count towards the Project-level [Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps).

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Ftweets%2Fsearch%2Fstream&method=get)