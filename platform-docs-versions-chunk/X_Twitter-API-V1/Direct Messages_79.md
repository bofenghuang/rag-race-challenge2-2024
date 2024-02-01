platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/typing-indicator-and-read-receipts/api-reference/new-read-receipt

POST direct\_messages/mark\_read

new-read-receipt

# POST direct\_messages/mark\_read

Marks a message as read in the recipient’s Direct Message conversation view with the sender.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/direct_messages/mark_read.json`

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
| **last\_read\_event\_id** (required) | The message ID of the most recent message to be marked read. All messages before it will be marked read as well. |
| **recipient\_id** (required) | The user ID of the user the message is from. |