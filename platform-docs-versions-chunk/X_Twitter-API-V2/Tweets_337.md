platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/migrate


### Manage Retweets  

The following tables compare the standard v1.1 and Twitter API v2 undo Retweet endpoint:

**Retweet a Tweet**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/statuses/retweet/:id.json | /2/users/:id/retweets |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | None<br><br>300 requests per 3-hour window (per user, per app). This is shared with the POST Tweet endpoint | 50 requests per 15 min (per user)<br><br>300 requests per 3-hour window (per user, per app). This is shared with the POST Tweet endpoint for manage Tweets. |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |

####   
Undo a Retweet

The following tables compare the standard v1.1 and Twitter API v2 undo Retweet endpoint:

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/statuses/unretweet/:id.json | /2/users/:id/retweets/:source\_tweet\_id |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | None | 50 requests per 15 min (per user) |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |