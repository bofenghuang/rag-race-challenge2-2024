platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/lookup/migrate/standard-to-twitter-api-v2


### Similarities

#### OAuth 1.0a User Context authentication method

The standard endpoint supports [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a), while the new Twitter API v2 users lookup endpoints supports both OAuth 1.0a User Context and [OAuth 2.0 Bearer Token](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0). Therefore, if you were previously using one of the standard v1.1 users lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

Depending on your authentication library/package of choice, Bearer Token authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate a Bearer Token, see [this OAuth 2.0 Bearer Token guide](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-only). 

#### Users per request limits

The standard v1.1 GET users/lookup endpoint allows you to specify 100 users per request. This also goes for the GET /users and GET /users/by endpoints. To specify a full 100 users, you will need to pass the ids (GET /users) parameter or the username (GET /users/by) parameter as a query parameter, and include the list of user IDs/usernames in a comma-separated list.