platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-retweet-id

POST statuses/retweet/:id

post-statuses-retweet-id

# POST statuses/retweet/:id

Retweets a tweet. Returns the original Tweet with Retweet details embedded.

_Usage Notes_:

* This method is subject to update limits. A HTTP 403 will be returned if this limit as been hit.
* Twitter will ignore attempts to perform duplicate retweets.
* The retweet\_count will be current as of when the payload is generated and may not reflect the exact count. It is intended as an approximation.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/statuses/retweet/:id.json`