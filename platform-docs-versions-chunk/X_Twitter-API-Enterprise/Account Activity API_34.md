platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries


### Retry timeline

The Account Activity API will retry up to three times over a five-minute period until a 200 response is received.  Refer to the table below for more details. After around five minutes, the activity cannot be resent through the Account Activity API. You will need to use other Twitter endpoints to collect missed data. For example, the [search APIs](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview) can be used to retrieve relevant Tweets, Retweets, Quote Tweets, Mentions, and Replies. Missed Direct Messages can be retrieved with [this endpoint](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events).

#### Retries timeline

|     |
| --- |
| Activity created, POST to the webhook URL from Account Activity API and times out in three seconds. |
| Wait three seconds after previous timeout finishes, then POST to the webhook URL from Account Activity API and times out in three seconds. |
| Wait 27 seconds after previous timeout finishes, then POST to the webhook URL from Account Activity API and times out in three seconds. |
| Wait 242 seconds after previous timeout finishes, then POST to the webhook URL from Account Activity API and times out in three seconds |
| The Account Activity API will stop attempting to POST after this. Client must use other Twitter endpoints to recover data. |