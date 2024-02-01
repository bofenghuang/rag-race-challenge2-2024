platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-lookup

GET friendships/lookup

get-friendships-lookup

# GET friendships/lookup

Returns the relationships of the authenticating user to the comma-separated list of up to 100 screen\_names or user\_ids provided. Values for `connections` can be: `following`, `following_requested`, `followed_by`, `none`, `blocking`, `muting`.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/friendships/lookup.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |