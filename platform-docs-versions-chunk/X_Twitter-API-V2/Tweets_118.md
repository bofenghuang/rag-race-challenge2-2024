platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction


### Recent search

The recent search endpoint allows you to programmatically access filtered public Tweets posted over the last week, and is available to all developers who have a developer account and are using keys and tokens from an [App](https://developer.twitter.com/en/docs/apps) within a [Project](https://developer.twitter.com/en/docs/projects).

You can authenticate your requests with [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). However, if you would like to receive private metrics, or a breakdown of organic and promoted metrics within your Tweet results, you will have to use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and pass user Access Tokens that are associated with the user that published the given content. 

This endpoint can deliver up to 100 Tweets per request in reverse-chronological order, and [pagination](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/paginate) tokens are provided for paging through large sets of matching Tweets. 

When using a Project with regular access, you can use the basic set of [operators](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-rule) and can make queries up to 512 characters long. When using a Project with Enterprise access, you have access to additional operators. Projects with Enterprise Access can make queries up to 4096 characters long.

Learn more about [access levels](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level).