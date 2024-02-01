platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-reverse-chronological

GET /2/users/:id/timelines/reverse\_chronological

# GET /2/users/:id/timelines/reverse\_chronological

Allows you to retrieve a collection of the most recent Tweets and Retweets posted by you and users you follow. This endpoint can return every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdTimeline&params=%28%27tweet.fields%21%27created_at%27%7Eexpansions%21%27author_id%27%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Ftimelines%2Freverse_chronological&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/timelines/reverse_chronological`