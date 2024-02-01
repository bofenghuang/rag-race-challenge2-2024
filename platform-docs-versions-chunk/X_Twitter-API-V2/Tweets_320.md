platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/introduction


### Manage Retweets

The manage Retweets endpoints enable you to Retweet or undo a Retweet of a specified Tweet on behalf of an authenticated account. For this endpoint group, there are two methods available POST and DELETE. The POST method allows you to Retweet a Tweet, and the DELETE method will enable you to undo a Retweet of a given Tweet.

Since you are making requests on behalf of a user, you must authenticate these endpoints with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and utilize the user Access Tokens associated with the user you are making the request on behalf of. You can generate this user Access Token using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) (OAuth 1.0a) or using the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0). You can Retweet a Tweet from your account or an account of an authenticated user. With both endpoints, there is a user rate limit of 50 requests per 15 minutes per endpoint.

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Fretweets&method=post)