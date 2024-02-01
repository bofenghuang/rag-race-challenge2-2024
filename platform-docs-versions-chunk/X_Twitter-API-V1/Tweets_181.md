platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-update

POST collections/update

post-collections-update

# POST collections/update

Update information concerning a Collection owned by the currently authenticated user.

Partial updates are not currently supported: please provide `name`, `description`, and `url` whenever using this method. Omitted `description` or `url` parameters will be treated as if an empty string was passed, overwriting any previously stored value for the Collection.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/collections/update.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |