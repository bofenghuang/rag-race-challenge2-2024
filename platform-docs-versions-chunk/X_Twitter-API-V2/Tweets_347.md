platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference

API reference

## API reference index

For the complete API reference, select an endpoint from the list:  
 

### Retweets lookup

|     |     |
| --- | --- |
| **Users who have Retweeted a Tweet** | [GET /2/tweets/:id/retweeted\_by](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/get-tweets-id-retweeted_by) |
| **Retweets of a Tweet** | [GET /2/tweets/:id/retweets](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/get-tweets-id-retweets) |

###   
Manage Retweets

|     |     |
| --- | --- |
| **Allows a user ID to Retweet a Tweet** | `[POST /2/users/:id/retweets](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/post-users-id-retweets)` |
| **Allows a user ID to undo a Retweet** | `[DELETE /2/users/:id/retweets/:source_tweet_id](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/delete-users-id-retweets-tweet_id)` |