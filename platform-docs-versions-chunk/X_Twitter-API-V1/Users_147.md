platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-subscribers

GET lists/subscribers

get-lists-subscribers

# GET lists/subscribers

subscribers/\*

Returns the subscribers of the specified list. Private list subscribers will only be shown if the authenticated user owns the specified list.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/lists/subscribers.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 180 |
| Requests / 15-min window (app auth) | 15  |