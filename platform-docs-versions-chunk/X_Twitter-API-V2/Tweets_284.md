platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/introduction


## Introduction

Volume streams consist of two streaming endpoints that deliver a random sample of publicly available Tweets in real-time. They are available to Enterprise levels of access only.

* 1% sampled stream.
* 10% sampled stream. Commonly referred to as the "Decahose."

These are referred to as "volume streams" because they both deliver large volumes of data. Even the 1% stream can emit many dozens of Tweets every second. With these streams, you can identify and track trends, monitor general sentiment, monitor global events, and much more.   

These streaming endpoints deliver [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) through a persistent HTTP GET connection and use [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0) authentication. With Essential access, you can have one connection at a time. With all levels of access, connection requests can be made up to 50 times per 15-minute window.

These volume stream endpoints support edited Tweets. These endpoints will deliver edited Tweets, along with its edit history, including an array of Tweet IDs. For Tweets with no edit history, this array will hold a single ID. For Tweets that have been edited, this array contains multiple IDs, arranged in ascending order reflecting the order of edits, with the most recent version in the last position of the array. To learn more about how Tweet edits work, see the [Tweet edits fundamentals](https://developer.twitter.com/en/docs/twitter-api/tweet-edits) page. 

_To use these APIs, you must first set up an account with our enterprise sales team._

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/quick-start/sampled-stream)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/tweets/sample/stream&method=get)