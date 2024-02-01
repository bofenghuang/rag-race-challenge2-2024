platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features


## Backfill 

The Backfill feature is used to request up to 5 minutes of stream data that is missed after a disconnect, and is available on PowerTrack and Volume streams as an _optional_ feature.

To request backfill, you need to add a ‘backfillMinutes=number’ parameter to your connection request, where ‘number’ is the number of minutes (1-5, whole numbers only) to backfill when the connection is made. For example, if you disconnect for 90 seconds, you should add ‘backfillMinutes=2’ to your connection request. Since this request will provide backfill for 2 minutes, including for the 30-second period before you disconnected, your _consumer app must be tolerant of duplicate data_.

An example PowerTrack connection request URL, requesting a 5 minute backfill, looks like:

https://gnip-stream.twitter.com/stream/powertrack/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json?backfillMinutes=5

**NOTES:**

* You do have the option to always use ‘backfillMinutes=5’ when you connect, then handling any duplicate data that is provided.
    
* If you are disconnected for more than five minutes, you can recover data using the Recovery.