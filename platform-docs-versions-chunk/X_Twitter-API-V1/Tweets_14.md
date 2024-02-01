platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/overview

Overview

**Please note:**

We've recently released the following endpoints within the [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api).

| v1.1 endpoints | Corresponding v2 endpoints |     |
| --- | --- | --- |
| [GET statuses/lookup](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-lookup)   <br>[GET statuses/show/:id](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-show-id) | [Tweet lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/migrate) |
| [POST statuses/update](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update)  <br>[POST statuses/destroy/:id](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-destroy-id) | [Manage Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/migrate) |
| [GET favorites/list](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-favorites-list)  <br>[POST favorites/create](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-create)   <br>[POST favorites/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-destroy) | [Likes](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/migrate) |
| [GET statuses/retweets/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets-id)   <br>[GET statuses/retweeters/:ids](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids)  <br>[POST statuses/retweet/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-retweet-id)   <br>[POST statuses/unretweet/:id](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id) | [Retweets](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/migrate) |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

**Important note:**

This endpoint has been updated to include Tweet edit metadata. Learn more about these metadata on the ["Edit Tweets" fundamentals page](https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets).