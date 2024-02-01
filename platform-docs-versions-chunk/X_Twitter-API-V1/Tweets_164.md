platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-create

POST collections/create

post-collections-create

# POST collections/create

Create a Collection owned by the currently authenticated user.

The API endpoint may refuse to complete the request if the authenticated user has exceeded the total number of allowed collections for their account.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/collections/create.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |