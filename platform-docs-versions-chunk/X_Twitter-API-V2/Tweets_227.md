platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule


## Building rules for filtered stream

The filtered stream endpoints deliver filtered Tweets to you in real-time that match on a set of rules that are applied to the stream. Rules are made up of operators that are used to match on a variety of Tweet attributes.

Multiple rules can be applied to a stream using the [POST /tweets/search/stream/rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules) endpoint. Once you’ve added rules and connect to your stream using the [GET /tweets/search/stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream) endpoint, only those Tweets that match your rules will be delivered in real-time through a persistent streaming connection. You do not need to disconnect from your stream to add or remove rules. 

To learn more about how to create high-quality rules, visit the following tutorial:  
[Building high-quality filters for getting Twitter data](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/building-high-quality-filters)