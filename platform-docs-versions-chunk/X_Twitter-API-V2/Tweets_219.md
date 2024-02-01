platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction


## Introduction

The filtered stream endpoint group enables developers to filter the real-time stream of public Tweets. This endpoint group’s functionality includes multiple endpoints that enable you to create and manage rules, and apply those rules to filter a stream of real-time Tweets that will return matching public Tweets. This endpoint group allows users to listen for specific topics and events in real-time, monitor the conversation around competitions, understand how trends develop in real-time, and much more.

Developers can use the REST [rules endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules) to add and remove rules to a persistent stream connection without needing to disconnect. These [rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule) can be created with operators that match on Tweet attributes such as message keywords, hashtags, and URLs. Operators and rule clauses can be combined with boolean logic and parentheses to help refine the filter’s matching behavior. 

Once you've added a set of rules, you can [establish a streaming connection](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream) which will start to deliver [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) in JSON format through a persistent HTTP Streaming connection. You will only receive content matching your rules while connected to the stream.

The filtered search endpoint supports edited Tweets. This endpoint will deliver edited Tweets that match one or more of your filters, along with its edit history, including an array of Tweet IDs. For Tweets with no edit history, this array will hold a single ID. For Tweets that have been edited, this array contains multiple IDs, arranged in ascending order reflecting the order of edits, with the most recent version in the last position of the array. To learn more about how Tweet edits work, see the [Tweet edits fundamentals](https://developer.twitter.com/en/docs/twitter-api/tweet-edits) page. 

Certain aspects of the filtered stream endpoint are limited by [access level](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level):

**Pro access**

* 1000 rules per stream
* 100 requests per 15 minutes when using the POST /2/tweets/search/stream/rules endpoint to add rules
* Can use all operators when building your rule
* Can build rules up to 1024 characters in length  
     

**Enterprise access**

* 2500+ rules per stream
* 450 requests per 15 minutes when using the POST /2/tweets/search/stream/rules endpoint to add rules
* Tweets/second delivery cap is set at access level for connections
* Can use all operators when building your rule
* Can build rules up to 2048 characters in length
* Can use the [recovery and redundancy features](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/recovery-and-redundancy-features) to maximize up-time and recover lost data in case of an outage

The returned Tweets from filtered stream count towards the monthly [Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps).

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/tweets/search/stream&method=get)

[Build a dashboard to find insights from Twitter data](https://developer.twitter.com/en/docs/tutorials/developer-guide--twitter-api-toolkit-for-google-cloud1)