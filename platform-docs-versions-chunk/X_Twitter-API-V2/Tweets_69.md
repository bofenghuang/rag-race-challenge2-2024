platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction


### User mention timeline

The user mention timeline endpoint allows you to request Tweets mentioning a specific Twitter user, for example, if a Twitter account mentioned @TwitterDev within a Tweet. This will also include replies to Tweets by the user requested. Retrieving a user's mentions allows you to build experiences such as quickly discovering who is replying to a users' Tweets, mentioning or to create engagement workflows with their Tweets programmatically. The endpoint allows you to request to a single user's most recent mentions and replies, similar to what may be seen in a user's [notifications for mentions](https://twitter.com/notifications/mentions) on Twitter.

The user mention timeline is a REST endpoint that receives a single path parameter to indicate the desired user (by user ID). The endpoint can return the 800 most recent mentions for that user.

Tweets are delivered in reverse-chronological order, starting with the most recent. Results are [paginated](https://developer.twitter.com/en/docs/twitter-api/pagination.html) in up to 100 Tweets per page. Pagination tokens are provided for paging through large sets of Tweets. The Tweet IDs of the newest and the oldest Tweets included in the given page are also provided as metadata, which can also be used for polling timelines for recent Tweets, or for navigating through the timeline similar to the v1.1 [mentions\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-mentions_timeline) endpoint. The endpoint also supports the ability to specify start\_time and end\_time parameters to receive Tweets that were created within a certain window of time. 

To successfully make a request to this endpoint, you will need to authorize your request with the [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), or [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) authentication methods. You must use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE when requesting non public metrics, promoted metrics or a protected user's timeline. 

The user mention timeline endpoint supports [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) parameters, and returns the [new JSON data format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/quick-start.html)

[Jump to example requests](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Ftweets&method=get)