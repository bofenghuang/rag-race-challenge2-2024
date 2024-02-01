platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-curate

POST collections/entries/curate

post-collections-entries-curate

# POST collections/entries/curate

Curate a Collection by adding or removing Tweets in bulk. Updates must be limited to 100 cumulative additions or removals per request.

Use [POST collections / entries / add](https://developer.twitter.com/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-add) and [POST collections / entries / remove](https://developer.twitter.com/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-remove) to add or remove a single Tweet.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/collections/entries/curate.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |