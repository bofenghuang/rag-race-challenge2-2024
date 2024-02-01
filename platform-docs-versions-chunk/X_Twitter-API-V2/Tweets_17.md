platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/migrate/standard-to-twitter-api-v2


### Similarities

#### OAuth 1.0a User Context authentication method

The standard endpoint supports [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a), while the new Twitter API v2 Tweet lookup endpoint supports both OAuth 1.0a User Context and [OAuth 2.0 App-Only](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0). Therefore, if you were previously using one of the standard v1.1 Tweet lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

Depending on your authentication library/package of choice, App-Only authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate an App Access Token, see [this OAuth 2.0 App-only guide](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only).   
 

#### Tweets per request limits

The v1.1 [GET statuses/lookup](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-lookup) endpoint allows you to specify 100 Tweets per request. This also goes for the GET /tweets endpoint. To specify a full 100 Tweets, you will need to pass the ids parameter as a query parameter rather than a path parameter and include the list of [Tweet IDs](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-ids) in a comma-separated list.   
 

**Support for Tweet edit history and metadata**  

Both versions provide metadata that describes any edit history. Check out the [Tweet lookup API References](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference) and the [Edit Tweets fundamentals page](https://developer.twitter.com/en/docs/twitter-api/edit-tweets) for more details.