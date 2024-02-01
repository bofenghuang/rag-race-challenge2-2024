platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate/standard-to-twitter-api-v2


### Similarities

#### OAuth 1.0a User Context and OAuth 2.0 App-Only authentication

The v1.1 search/tweets and the Twitter API v2 recent search endpoint support both [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) and [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0). 

Therefore, if you were previously using the standard v1.1 search endpoint you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

Depending on your authentication library/package of choice, App-Only authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate an App Access Token see this [OAuth 2.0 App-Only guide](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only). 

If you would like to take advantage of the ability to pull private or advertising metrics with the Twitter API v2 endpoint, you will need to use OAuth 1.0a User Context, and pass the user access tokens related to the user who posted the Tweet for which you would like to pull metrics. 

  
**Support for Tweet edit history and metadata**

Both versions provide metadata that describes any edit history. Check out the [search API References](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference) and the [Tweet edits fundamentals page](https://developer.twitter.com/en/docs/twitter-api/tweet-edits) for more details.