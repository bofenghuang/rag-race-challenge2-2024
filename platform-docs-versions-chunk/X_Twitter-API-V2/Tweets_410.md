platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference

API reference

## API reference index

For the complete API reference, select an endpoint from the list:  
 

### Likes lookup

|     |     |
| --- | --- |
| **Users who have liked a Tweet** | [GET /2/tweets/:id/liking\_users](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/get-tweets-id-liking_users) |
| **Tweets liked by a user** | [GET /2/users/:id/liked\_tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/get-users-id-liked_tweets) |

### Manage Likes

|     |     |
| --- | --- |
| **Allows a user ID to like a Tweet** | `[POST /2/users/:id/likes](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/post-users-id-likes)` |
| **Allows a user ID to unlike a Tweet** | `[DELETE /2/users/:id/likes/:tweet_id](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/delete-users-id-likes-tweet_id)` |