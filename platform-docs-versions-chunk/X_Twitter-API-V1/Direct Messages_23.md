platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/get-event

GET direct\_messages/events/show

get-event

# GET direct\_messages/events/show

Returns a single Direct Message event by the given id.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/direct_messages/events/show.json`

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
| **id** (required) | The id of the Direct Message event that should be returned. |

## Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -X GET /1.1/direct_messages/events/show.json?id=110