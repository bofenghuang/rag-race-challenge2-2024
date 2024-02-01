platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-add

POST collections/entries/add

post-collections-entries-add

# POST collections/entries/add

Add a specified Tweet to a Collection.

A collection will store up to a few thousand Tweets. Adding a Tweet to a collection beyond its allowed capacity will remove the oldest Tweet in the collection based on the time it was added to the collection.

Use [POST collections / entries / curate](https://developer.twitter.com/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-curate) to add Tweets to a Collection in bulk.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/collections/entries/add.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |