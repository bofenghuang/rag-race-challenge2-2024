platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/quote-tweets/introduction


### Quote Tweets lookup

The Quote Tweets lookup endpoint gives the Quote Tweets for a given Tweet ID.  This allows developers that build apps and clients to get the Quote Tweets for a Tweet quickly and efficiently. It also makes it easy for researchers to study the full conversation around a Tweet including all its Quote Tweets.

Here is a Quote Tweet for a Tweet from @TwitterAPI:

> Today, OAuth 2.0 and new fine-grained permission scopes are available to all developers for Twitter API v2 endpoints. [https://t.co/rNxC0GQDoP](https://t.co/rNxC0GQDoP)
> 
> — Twitter API (@TwitterAPI) [December 14, 2021](https://twitter.com/TwitterAPI/status/1470836235413295107?ref_src=twsrc%5Etfw)

The Quote Tweets lookup endpoint is a REST endpoint that takes a single path parameter to indicate the desired Tweet (by Tweet ID). 

Tweets are delivered in reverse-chronological order, starting with the most recent. Results are [paginated](https://developer.twitter.com/en/docs/twitter-api/pagination.html) up to 100 Tweets per page (10 Tweets by default). Pagination tokens are provided for paging through large sets of Tweets.

The Quote Tweets endpoint supports [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) parameters, and returns the [new JSON data format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

This endpoint will always return the most recent edit, along with the edit history. Any Tweet collected after its 30-minute edit window will represent its final version and will include an array of IDs for all Tweets in its edit history. For Tweets with no edit history, this array will hold a single ID.

To successfully make a request to this endpoint, you will need to authorize your request with the [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), or [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) authentication methods. You must use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE when requesting non public metrics, promoted metrics or a protected user's timeline.

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/quote-tweets/quick-start.html)

[Jump to example requests](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Ftweets%2F%7Bid%7D%2Fquote_tweets&method=get)