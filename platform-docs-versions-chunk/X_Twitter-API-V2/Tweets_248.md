platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/recovery-and-redundancy-features


### Recovering missed data after a disconnection: Recovery

If you are using a Project with Enterprise access, you can use the Recovery feature to recover missed data within the last 24 hours if you are unable to reconnect with the 5 minute backfill window.

The streaming recovery feature allows you to have an extended backfill window of 24 hours. Recovery enables you to 'replay' the time period of missed data. A recovery stream is started when you make a connection request using 'start\_time' and 'end\_time' request parameters. Once connected, Recovery will re-stream the time period indicated, then disconnect.  

You will be able to make 2 concurrent requests to recovery at the same time, i.e. “two recovery jobs”. Recovery works technically in the same way as backfill, except a start and end time is defined. A recovery period is for a single time range.

|     |     |     |
| --- | --- | --- |
| **Name** | **Type** | **Description** |
| start\_time | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339).<br><br>Date in UTC signifying the start time to recover from. |
| end\_time | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339).<br><br>Date in UTC signifying the end time to recover to. |

  
Example request URL: [https://api.twitter.com/2/tweets/search/stream?start\_time=2022-07-12T15:10:00Z&end\_time=2022-07-12T15:20:00Z](https://api.twitter.com/2/tweets/search/stream?start_time=1985-04-12T23:20:50.52Z&end_time=1985-04-13T00:20:50.52Z)