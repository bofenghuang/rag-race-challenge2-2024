platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-create

POST favorites/create

post-favorites-create

# POST favorites/create

Note: favorites are now known as _likes_.

Favorites (_likes_) the Tweet specified in the ID parameter as the authenticating user. Returns the favorite Tweet when successful.

The process invoked by this method is asynchronous. The immediately returned Tweet object may not indicate the resultant favorited status of the Tweet. A 200 OK response from this method will indicate whether the intended action was successful or not.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/favorites/create.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24-hour window | 1000 per user; 1000 per app |