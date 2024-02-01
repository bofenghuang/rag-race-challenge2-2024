platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits


### POST endpoints

The standard API rate limits described in this table refer to POST endpoints. These rate limits apply to the standard API endpoints only, does not apply to premium APIs.

|     |     |     |     |
| --- | --- | --- | --- |
| Endpoint | Rate limit window | Rate limit per user | Rate limit per app |
| [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update) | 3 hours\* | 300\* | 300\* |
| [POST statuses/retweet/:id](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-retweet-id) | 3 hours\* | 300\* | 300\* |
| [POST favorites/create](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-favorites-create) | 24 hours | 1000 | 1000 |
| [POST friendships/create](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create) | 24 hours | 400 | 1000 |
| [POST direct\_messages/events/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) | 24 hours | 1000 | 15000 |

  
**Please note**

The 300 per 3 hours is with the POST statuses/update and POST statuses/retweet/:id endpoints is a combined limit. You can only post 300 Tweets or Retweets during a 3 hour period. 

For example, if your Twitter app makes 200 requests to the POST statuses/update endpoint within a three hour period, your app will only be able to make 100 requests to the POST statuses/retweet/:id endpoint during that period.