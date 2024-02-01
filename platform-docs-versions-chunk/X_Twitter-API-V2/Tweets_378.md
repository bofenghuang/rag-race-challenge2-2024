platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/quote-tweets/api-reference/get-tweets-id-quote_tweets

GET /2/tweets/:id/quote\_tweets

# GET /2/tweets/:id/quote\_tweets

Returns Quote Tweets for a Tweet specified by the requested Tweet ID.  
  
The Tweets returned by this endpoint count towards the Project-level [Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps).

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=findTweetsThatQuoteATweet&params=%28%27id%21%2720%27%7Emax_results%21%2710%27%7Etweet.fields%21%27created_at%27%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Ftweets%2F%7Bid%7D%2Fquote_tweets&method=get) 

### Endpoint URL

`https://api.twitter.com/2/tweets/:id/quote_tweets`