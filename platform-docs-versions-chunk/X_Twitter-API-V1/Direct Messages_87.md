platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/conversation-management/guides/initiated-via

## initiated\_via object

|     |     |
| --- | --- |
| initiated\_via.tweet\_id | The ID of the Tweet with Direct Message Prompt the event was initiated from if one was used. |
| initiated\_via.welcome\_message\_id | The ID of the Welcome Message immediately preceding the event if one was used. |

**Note:** Direct Messages are never referenced as an entity type under the “initiated\_via” object. Developers should continue to rely on IDs for ordering Direct Message events.