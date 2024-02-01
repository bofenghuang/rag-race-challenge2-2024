platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create

POST friendships/create

post-friendships-create

# POST friendships/create

Allows the authenticating user to follow (_friend_) the user specified in the ID parameter.

Returns the followed user when successful. Returns a string describing the failure condition when unsuccessful. If the user is already friends with the user a HTTP 403 may be returned, though for performance reasons this method may also return a HTTP 200 OK message even if the follow relationship already exists.

Actions taken in this method are asynchronous. Changes will be eventually consistent.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/friendships/create.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24-hour window | 400 per user; 1000 per app |