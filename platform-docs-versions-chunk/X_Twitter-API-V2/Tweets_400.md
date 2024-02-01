platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/migrate


### Manage Likes  

The v2 manage Likes endpoints replace the v1.1 [POST favorites/create](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-create) and [POST favorites/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-destroy) endpoints.

The following tables compare the standard v1.1 and Twitter API v2 manage Like endpoints:

#### Like a Tweet

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/favorites/create.json | /2/users/:id/likes |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 1000 requests per 24 hours (per user)<br><br>1000 requests per 24 hours (per App) | 50 requests per 15 min (per user)<br><br>1000 successful requests per 24 hours (per user, shared with DELETE) |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |

#### Unlike a Tweet

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/favorites/destroy.json | /2/users/:id/likes/:tweet\_id |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 1000 requests per 24 hours (per user)<br><br>1000 requests per 24 hours (per App) | 50 requests per 15 min (per user)<br><br>1000 successful requests per 24 hours (per user, shared with POST) |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |