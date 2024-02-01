platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/api-reference/get-tweets-compliance-stream

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `partition`  <br> Required | number | Must be set to 1, 2, 3 or 4. Tweet compliance events are split across 4 partitions, so 4 separate streams are needed to receive all events. |
| `backfill_minutes`  <br> Optional | number | By passing this parameter, you can recover up to five minutes worth of data that you might have missed during a disconnection. The backfilled events will automatically flow through a reconnected stream, with older events generally being delivered before any newer events. You must include a whole number between 1 and 5 as the value to this parameter. nThis feature will deliver all events that published during the timeframe selected, meaning that if you were disconnected for 90 seconds, and you requested two minutes of backfill, you will receive 30 seconds worth of duplicate events. Due to this, you should make sure your system is tolerant of duplicate data. |