platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/rate-limits


###   
Enterprise rate limits per window

| Product | Endpoint | Rate limit |
| --- | --- | --- |
| PowerTrack API | Streaming endpoint | 60 requests per minute |
| Rules endpoint | 60 requests per minute aggregated across all /rules endpoints |
| Replay endpoint | 5 requests per 5 minutes |
| Historical PowerTrack API |     | 60 Jobs can be created per (UTC) day. |
|     | 30 Jobs can be created per hour. |
|     | 2 Jobs can be estimating concurrently. |
|     | 2 Jobs can be running concurrently. |
| Decahose API |     | 10 requests per minute |
| Streaming likes API |     | 10 requests per minute |
| Firehose API |     | 10 requests per minute |
| Account Activity API | POST account\_activity/webhooks | 15 requests per 15 minutes |
| GET account\_activity/webhooks | 15 requests per 15 minutes |
| PUT account\_activity/webhooks/:webhook\_id | 15 requests per 15 minutes |
| POST account\_activity/webhooks/:webhook\_id/subscriptions/all | 500 requests per 15 minutes |
| GET account\_activity/subscriptions/count | 15 requests per 15 minutes |
| GET account\_activity/webhooks/:webhook\_id/subscriptions/all | 500 requests per 15 minutes |
| GET account\_activity/webhooks/:webhook\_id/subscriptions/all/list | 50 requests per 15 minutes |
| DELETE account\_activity/webhooks/:webhook\_id | 15 requests per 15 minutes |
| DELETE /account\_activity/webhooks/:webhook\_id/subscriptions/:user\_id/all.json | 500 requests per 15 minutes |
| Replay | 5 requests per 15 minutes |
| Search API |     | Per minute rate limit will vary by contract |
|     | 20 requests per second aggregated across either the 30 day data and counts endpoints, or across the full-archive data and counts endpoints |
| Engagement API |     | Per minute rate limit will vary by contract |
| Compliance Firehose API |     | 10 requests per minute |
| Usage API |     | 2 requests per minute |