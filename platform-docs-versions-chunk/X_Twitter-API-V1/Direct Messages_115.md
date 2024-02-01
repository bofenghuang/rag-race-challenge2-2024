platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/customer-feedback/api-reference/create

POST feedback/create.json

create

# POST feedback/create.json

Sends Feedback prompt along with a Direct Message (DM) to a specified user. The DM message is required. Sending Feedback inherits the Direct Message restrictions and behavior from [POST direct\_messages/events/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event).

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | 1,000 and 1 per recipient |

**Note**

Handles can be added to an allowlist to receive more than 1 new feedback request per 24 hours. Please send a list of @handles to your account manager.