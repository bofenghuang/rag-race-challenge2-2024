platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/typing-indicator-and-read-receipts/api-reference/new-typing-indicator

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 1000 / 15 minutes |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **recipient\_id** (required) | The user ID of the user to receive the typing indicator. |

## Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -X POST /1.1/direct_messages/indicate_typing.json -d "recipient_id=3805104374"

## HTTP Response Codes[¶](#http-response-codes "Permalink to this headline")

Response contains no body.

| Code | Message |
| --- | --- |
| 204 | Typing indicator successfully sent. |
| 400 | Missing or invalid parameter(s) included in request. |