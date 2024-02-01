platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/api-reference/list-welcome-messages

GET direct\_messages/welcome\_messages/list

list-welcome-messages

# GET direct\_messages/welcome\_messages/list

Returns a list of Welcome Messages.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/direct_messages/welcome_messages/list.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **count** (optional) | Number of welcome messages to be returned. Max of 50. Default is 20. |
| **cursor** (optional) | For paging through result sets greater than 1 page, use the “next\_cursor” property from the previous request. |