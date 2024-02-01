platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/migrate/manage-dms-standard-to-twitter-api-v2


## 

Path: POST /2/dm\_conversations/with/:participant\_id/messages

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | POST direct\_messages/events/new (message\_create) | POST /2/dm\_conversations/with/:participant\_id/messages |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) | 1000 requests per user per 24 hours  <br>15000 requests per app per 24 hours | 200 requests per 15 minutes per user<br><br>1000 requests per user per 24 hours<br><br>15000 requests per app per 24 hours<br><br>These rate limits are shared across all dm\_conversations POST endpoints. |
| Supports group Direct Messages |     | ✔   |

**Create a new Direct Message group conversation and add a message to it**  

Path: POST /2/dm\_conversations

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | Not supported | POST /2/dm\_conversations |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) |     | 200 requests per 15 minutes per user<br><br>1000 requests per user per 24 hours<br><br>15000 requests per app per 24 hours<br><br>These rate limits are shared across all dm\_conversations POST endpoints. |
| Supports group Direct Messages |     | ✔   |

**Add a Direct Message to an existing conversation by ID**  

Path: POST /2/dm\_conversations/:dm\_conversation\_id/messages

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | Not supported | POST /2/dm\_conversations/:dm\_conversation\_id/messages |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) |     | 200 requests per 15 minutes per user<br><br>1000 requests per user per 24 hours<br><br>15000 requests per app per 24 hours<br><br>These rate limits are shared across all dm\_conversations POST endpoints. |
| Supports group Direct Messages |     | ✔   |