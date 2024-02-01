platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id

POST statuses/unretweet/:id

post-statuses-unretweet-id

# POST statuses/unretweet/:id

Untweets a retweeted status. Returns the original Tweet with Retweet details embedded.

**Usage Notes**:

* This method is subject to update limits. A HTTP 429 will be returned if this limit has been hit.
* The untweeted retweet status ID must be authored by the user backing the authentication token.
* An application must have write privileges to POST. A HTTP 401 will be returned for read-only applications.
* When passing a source status ID instead of the retweet status ID a HTTP 200 response will be returned with the same Tweet object but no action.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/statuses/unretweet/:id.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |