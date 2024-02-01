platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships

GET lists/memberships

get-lists-memberships

# GET lists/memberships

Returns the lists the specified user has been added to. If `user_id` or `screen_name` are not provided, the memberships for the authenticating user are returned.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/lists/memberships.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 75  |