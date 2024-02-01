platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/delete-users-id-retweets-tweet_id

DELETE /2/users/:id/retweets/:source\_tweet\_id

# DELETE /2/users/:id/retweets/:source\_tweet\_id

Allows a user or authenticated user ID to remove the Retweet of a Tweet.  
  
The request succeeds with no action when the user sends a request to a user they're not Retweeting the Tweet or have already removed the Retweet of.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdUnretweets&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%27id%21%27%27%7Esource_tweet_id%21%27%27%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Fretweets%2F%7Bsource_tweet_id%7D&method=delete) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/retweets/:source_tweet_id`