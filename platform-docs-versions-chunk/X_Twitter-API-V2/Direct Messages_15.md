platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/integrate


### Authentication

All Twitter API v2 endpoints require for you to authenticate your requests with a set of credentials, also known as keys and tokens. All Direct Messages are private and require user authorization to access them. 

These Direct Message endpoints require the use of [OAuth 2.0 Authorization Flow with PKCE](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/integrate#authentication) or [1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), which means that you must use a set of API keys and user Access Tokens to make a successful request. The Access Tokens must be associated with the user that you are requesting on behalf of. If you want to generate a set of Access Tokens for another user, they must authorize or authenticate your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).

Please note that OAuth user-context can be tricky to use. If you are not familiar with this authentication method, we recommend using a [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) or a tool like Postman to properly authenticate your requests. 

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. The Direct Messages lookup endpoints require these scopes:  dm.read, tweet.read, user.read

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.