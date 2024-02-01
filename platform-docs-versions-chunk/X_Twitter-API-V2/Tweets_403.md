platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/migrate/likes-lookup-standard-to-twitter-api-v21


### Similarities

#### **Authentication**

Both the standard v1.1 and Twitter API v2 Likes lookup endpoints use [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Bearer Token](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-only). Therefore, if you were previously using the [GET favorites/list endpoints](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-favorites-list) standard v1.1 endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version if you wish. 

Depending on your authentication library/package of choice, Bearer Token authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate a Bearer Token, see [this OAuth 2.0 Bearer Token guide](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-only).   
 

**Rate limits**

The standard v1.1 GET favorites/list endpoint has a 75 requests per 15 minutes per user rate limit. The corresponding liked Tweets endpoint in v2 also has this same rate limit. However, this v2 endpoint also has an additional rate limit of 75 requests per 15 minutes per App.