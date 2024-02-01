platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api


## Account Activity Replay API

Enterprise

The Account Activity Replay API is a data recovery tool that allows you to retrieve events from as far back as five days. It should be utilized to recover data in scenarios where your [webhook](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise) server misses events, -- whether due to disconnections lasting longer than the [retry window](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries), or for those disaster recovery scenarios where you need a few days to restore your system back to normal.

The Account Activity Replay API was developed for any scenario where you fail to ingest [activities](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/overview) for a period of time. It delivers activities to the same webhook used for the original real-time delivery of activities. This product is a recovery tool and not a backfill tool, which means events will only be replayed if a previous delivery of them was attempted. The Account Activity Replay API cannot deliver events for a time period prior to a subscription’s creation time.