platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/customer-feedback/api-reference/show

GET feedback/show/:id.json

show

# GET feedback/show/:id.json

Returns a single Feedback response for the specified ID in the URL.

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15 min window (user auth) | 180 |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **feedback\_id** (required) | Required in path. |

## Response Values[¶](#response-values "Permalink to this headline")

|     |     |
| --- | --- |
| **score** | The user provided score response. 1­5 if type is CSAT. 0­10 if type is NPS. |
| **text** | The user provided text response. |