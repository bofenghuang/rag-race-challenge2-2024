platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/introduction


### Manage Likes

The manage Likes endpoints enable you to like or unlike a specified Tweet on behalf of an authenticated account. For this endpoint group, there are two methods available POST and DELETE. The POST method allows you to like a Tweet, and the DELETE method will enable you to unlike a Tweet.

Since you are making requests on behalf of a user, you must authenticate these endpoints with [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) and use the Access Tokens associated with the user, which can be generated using the [3-legged OAuth flow](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). You can like a Tweet from your account or an account of an authenticated user. With both endpoints, there is a user rate limit of 50 requests per 15 minutes per endpoint.   
 

To access these endpoint, you must have an approved [developer account](https://developer.twitter.com/en/docs/developer-portal/overview). When authenticating, you must use keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started](https://developer.twitter.com/en/docs/twitter-api/getting-started) page.  
  

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)