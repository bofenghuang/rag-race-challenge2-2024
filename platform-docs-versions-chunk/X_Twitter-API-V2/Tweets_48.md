platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/migrate


## Comparing Twitter API’s manage Tweets endpoints

The v2 manage Tweets endpoints will replace the standard v1.1 [POST statuses/update](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update) and [POST statuses/destroy/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-destroy-id) endpoints. If you have code, apps, or tools that use the v1.1 version of the manage Tweets endpoints and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you.   

The following tables compare the standard v1.1 and Twitter API v2 manage Tweets endpoints:

**Create a Tweet**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/statuses/update.json | /2/tweets |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 User Context |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) | None<br><br>300 requests per 3-hour window per user, per app. Shared with the v1.1 POST Retweets endpoint. | 200 requests per 15 min per user<br><br>300 requests per 3-hour window per user, per app. Shared with the v2 POST Retweets endpoint. |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |

####   
Delete a Tweet

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/statuses/destroy/:id.json | /2/tweets/:id |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) | None | 50 requests per 15 min per user |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |