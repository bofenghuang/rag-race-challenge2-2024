platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/migrate


### Likes lookup  

#### Users who have liked a Tweet

The liked users endpoint is new functionality for v2, allowing you to get information about a Tweet’s liking users.

| Description | Twitter API v2 |
| --- | --- |
| HTTP methods supported | GET |
| Host domain | https://api.twitter.com |
| Endpoint path | /2/tweets/:id/liking\_users |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 2.0 Bearer Token<br><br>OAuth 1.0a User Context |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 75 requests per 15 min (per App)<br><br>75 requests per 15 min (per user) |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) | ✔️  |

####   
Tweets liked by a user

The following tables compare the standard v1.1 [GET favorites/list](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-favorites-list) endpoint and the Twitter API v2 liked Tweets endpoints:

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | GET | GET |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/favorites/list.json | /2/users/:id/liked\_tweets |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 2.0 Bearer Token<br><br>OAuth 1.0a User Context |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 75 requests per 15 min | 75 requests per 15 min (per App)<br><br>75 requests per 15 min (per user) |
| Data formats | Standard v1.1 format | [Twitter API v2 format](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary) (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |