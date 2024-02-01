platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent

GET /2/tweets/search/recent

# GET /2/tweets/search/recent

The recent search endpoint returns Tweets from the last seven days that match a search query.  
  
The Tweets returned by this endpoint count towards the Project-level [Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps).

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=tweetsRecentSearch&params=%28%27query%21%27from%3ATwitterDev%27%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Ftweets%2Fsearch%2Frecent&method=get) 

### Endpoint URL

`https://api.twitter.com/2/tweets/search/recent`