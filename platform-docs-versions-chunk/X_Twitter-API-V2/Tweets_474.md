platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/introduction


## Introduction

Many people want the benefit of hiding replies to improve the quality of their conversations. Sometimes it’s difficult or overwhelming to do so without help, particularly when people receive a large number of replies, when those replies contain offensive or abusive language, or when they want to confine certain conversations to specific groups like close friends.

This endpoint gives you the ability to programmatically hide or unhide replies using criteria you define. Just like the functionality in the main Twitter experience, replies will be hidden from the main conversation but still visible on a separate page. You can use the endpoint to create apps to help people hide replies they don’t find valuable.

The hide replies endpoint uses either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) authentication. If successful, the endpoint hides a single Reply that was published in a Tweet conversation that was initiated by an authenticated user. Each conversation supports hiding up to 725 Tweets.

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/quick-start)

[Jump to example requests](https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/api-reference/put-tweets-id-hidden)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Ftweets%2F%7Bid%7D%2Fhidden&method=put)