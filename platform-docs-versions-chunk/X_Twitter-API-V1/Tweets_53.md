platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets-id

GET statuses/retweets/:id

get-statuses-retweets-id

# GET statuses/retweets/:id

Returns a collection of the 100 most recent retweets of the Tweet specified by the `id` parameter.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/statuses/retweets/:id.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 300 |