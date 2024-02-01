platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules

POST /2/tweets/search/stream/rules

# POST /2/tweets/search/stream/rules

Add or delete rules to your stream.  
  
Once you've added a rule or rules to your stream, you can retrieve all of the Tweets that match these rules by using the [GET /tweets/search/stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream) endpoint.  
  
To learn how to build a rule, please read our guide on [building a rule](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule).  
  
To create one or more rules, submit an `add` JSON body with an array of rules and operators. Similarly, to delete one or more rules, submit a `delete` JSON body with an array of list of existing rule IDs.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Ftweets%2Fsearch%2Fstream%2Frules&method=post)