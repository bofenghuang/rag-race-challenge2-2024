platform: X
topic: Twitter-API-Enterprise
subtopic: Decahose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Decahose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/guides/recovery-and-redundancy


## Recovery

#### Overview 

Recovery is a data recovery tool (not to be used for primary data collection) that provides streaming access to a rolling 5-day window of recent Twitter historical data. It should be utilized to recover data in scenarios where your consuming application misses data in the realtime stream, whether due to disconnecting for a short period, or for any other scenario where you fail to ingest realtime data for a period of time.

#### Using Recovery 

With the Recovery stream, your app can make requests to it that operate in the same manner as requests to the realtime streams. However, your app must specify parameters in the URL that indicate the time window you are requesting. In other words, a Recovery request asks the API for "Tweets from time A to time B." These Tweets are then delivered through your streaming connection in a manner that mimics the realtime stream, but at a slightly slower-than-realtime rate. See below for example:

  
"https://stream-data-api.twitter.com/stream/powertrack/accounts/someAccountName/publishers/twitter/powertrack.json?startTime=2023-07-05T17:09:12.070Z"

Tweets are delivered beginning with the first (oldest) minute of the specified time period, continuing chronologically until the final minute is delivered. At that point, aRecovery Request Completed message is sent through the connection, and the connection is then closed by the server. If your request begins at a time of day where little or no matching results occurred, there will likely be some period of time before the first results are delivered – data will be delivered when Recovery encounters matches in the portion of the archive being processed at that time. When no results are available to deliver, the stream will continue sending carriage-return, or "heartbeats", through the connection to prevent you from timing out.

Recovery is intended as a tool for easily recovering data missed due to short disconnects, not for very long time periods like an entire day. If the need to recover data for long periods arises, we recommend breaking longer requests into shorter time windows (e.g. two hours) to reduce the possibility of being disconnected mid-request due to internet volatility or other reasons, and to provide more visibility into the progress of long requests.

#### Data Availability

You can use the Recovery feature to recover missed data within the last 24 hours if you are unable to reconnect with the 5 minute backfill window.

The streaming recovery feature allows you to have an extended backfill window of 24 hours. Recovery enables you to ‘recover’ the time period of missed data. A recovery stream is started when you make a connection request using 'start\_time' and 'end\_time' request parameters. Once connected, Recovery will re-stream the time period indicated, then disconnect.  

You will be able to make 2 concurrent requests to recovery at the same time, i.e. “two recovery jobs”. Recovery works technically in the same way as backfill, except a start and end time is defined. A recovery period is for a single time range.