platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/migrate/standard-to-twitter-api-v2


## 

Path: GET /2/dm\_conversations/with/:participant\_id/dm\_events

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | GET <br><br>/1.1/direct\_messages/events/list | GET /2/dm\_conversations/with/:participant\_id/dm\_events |
| How much event history is available | 30 days | No limit |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) | 15 requests per 15 minutes | 300 requests per 15 minutes  <br>Rate limit is applied across all three GET endpoints |

**Get all messages by conversation ID**   

Path: GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | Not supported. V1.1 can return messages from one-to-one conversations only and there is no support for retrieving events by conversation IDs. | GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events |
| How much event history is available | 30 days | No limit |
| Supports group conversations |     | ✔   |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) | 15 requests per 15 minutes | 300 requests per 15 minutes  <br>Rate limit is applied across all three GET endpoints |
|     |     |

**Get all events across an authenticated user's conversations, both one-to-one and group conversations**  

Path: GET /2/dm\_events

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | GET /1.1/direct\_messages/events/list  <br>  <br>V1.1 can return messages from one-to-one conversations only. | GET /2/dm\_events |
| How much event history is available | 30 days | 30 days |
| Supports group conversations |     | ✔   |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) | 15 requests per 15 minutes | 300 requests per 15 minutes  <br>Rate limit is applied across all three GET endpoints |
|     |     |