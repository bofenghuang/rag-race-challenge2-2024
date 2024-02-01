platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/new-event

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24-hour window | 1000 per user; 15000 per app |

## Direct Message Rate Limiting[¶](#direct-message-rate-limiting "Permalink to this headline")

When a message is received from a user you may send up to 5 messages in response within a 24 hour window. Each message received resets the 24 hour window and the 5 allotted messages. Sending a 6th message within a 24 hour window or sending a message outside of a 24 hour window will count towards rate-limiting. This behavior only applies when using the POST direct\_messages/events/new endpoint.