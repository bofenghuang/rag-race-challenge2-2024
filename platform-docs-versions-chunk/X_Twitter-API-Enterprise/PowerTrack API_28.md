platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features


## Recovery 

#### Overview 

Recovery is a data tool that provides streaming access to a rolling window of recent Twitter historical data. It should be utilized to recover data in scenarios where your consuming application misses data in the real time stream, whether due to disconnecting for a short period, or for any other scenario where you fail to ingest realtime data for a period of time.

There are different varieties of Recovery streams, corresponding to different types of realtime streams that they complement. PowerTrack Recovery streams are provided to allow customers using realtime PowerTrack to recover data they miss, using the same rules as they use in realtime.

#### Using Recovery 

With the Recovery stream, your app can make requests to it that operate in the same manner as requests to existing realtime streams. However, your app must specify parameters in the URL that indicate the time window you are requesting. In other words, a Recovery request asks for “Posts from time A to time B.” These Posts are then delivered through your streaming connection in a manner that mimics the realtime stream.

Posts are delivered beginning with the first minute of the specified time period, continuing until the final minute is delivered. At that point, a “Recovery Request Completed” message is sent through the connection, and the connection is then closed by Gnip. If your request begins at a time of day where little or no matching results occurred, there will likely be some period of time before the first results are delivered – data will be delivered when Recovery encounters matches in the portion of the archive being processed at that time. When no results are available to deliver, the stream will continue sending carriage-return “heartbeats” through the connection to prevent you from timing out.

Recovery is intended as a tool for easily recovering data missed due to short disconnects, not for very long time periods like entire days. If the need to recover data for long periods arises, we recommend breaking longer requests into shorter time windows (e.g. two hours) to reduce the possibility of being disconnected mid-request due to internet volatility or other reasons, and to provide more visibility into the progress of long requests.

#### Data availability

You can use the Recovery feature to recover missed data within the last 24 hours if you are unable to reconnect with the 5 minute backfill window.

The streaming recovery feature allows you to have an extended backfill window of 24 hours. Recovery enables you to ‘recover’ the time period of missed data. A recovery stream is started when you make a connection request using 'startTime' and 'endTime' request parameters. Once connected, Recovery will re-stream the time period indicated, then disconnect.  

You will be able to make 2 concurrent requests to recovery at the same time, i.e. “two recovery jobs”. Recovery works technically in the same way as backfill, except a start and end time is defined. A recovery period is for a single time range.

| Name | Type | Description |
| --- | --- | --- |
| startTime | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339).<br><br>Date in UTC signifying the start time to recover from. |
| endTime | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339).<br><br>Date in UTC signifying the end time to recover to. |

 [](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream)