platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/list-events

GET direct\_messages/events/list

list-events

# GET direct\_messages/events/list

Returns all Direct Message events (both sent _and_ received) within the last 30 days. Sorted in reverse-chronological order.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/direct_messages/events/list.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15/user |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **count** (optional) | Max number of events to be returned. 20 default. 50 max. |
| **cursor** (optional) | For paging through result sets greater than 1 page, use the “next\_cursor” property from the previous request. |