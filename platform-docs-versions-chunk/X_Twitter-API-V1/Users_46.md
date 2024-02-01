platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-list

GET mutes/users/list

get-mutes-users-list

# GET mutes/users/list

Returns an array of [user objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) the authenticating user has muted.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/mutes/users/list.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |