platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-outgoing

GET friendships/outgoing

get-friendships-outgoing

# GET friendships/outgoing

Returns a collection of numeric IDs for every protected user for whom the authenticating user has a pending follow request.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/friendships/outgoing`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |