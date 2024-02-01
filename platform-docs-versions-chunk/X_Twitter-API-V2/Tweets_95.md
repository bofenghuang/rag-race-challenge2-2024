platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-tweets

GET /2/users/:id/tweets

# GET /2/users/:id/tweets

Returns Tweets composed by a single user, specified by the requested user ID. By default, the most recent ten Tweets are returned per request. Using pagination, the most recent 3,200 Tweets can be retrieved.  
  
The Tweets returned by this endpoint count towards the Project-level [Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps).

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdTweets&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%27*%7E**id%21%272244994945%27%29%01*_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Ftweets&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/tweets`