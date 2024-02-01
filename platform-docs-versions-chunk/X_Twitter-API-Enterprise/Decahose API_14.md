platform: X
topic: Twitter-API-Enterprise
subtopic: Decahose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Decahose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/guides/recovery-and-redundancy

## Backfill

To request backfill, you need to add a backfillMinutes=N parameter to your connection request, where N is the number of minutes (1-5, whole numbers only) to backfill when the connection is made. For example, if you disconnect for 90 seconds, you should add backfillMinutes=2 to your connection request. Since this request will provide backfill for 2 minutes, including for the 30-second period before you disconnected, your _consumer app must be tolerant of duplicate data_.

An example Decahose connection request URL, requesting a 5 minute backfill to partition 1, looks like:

https://gnip-stream.twitter.com/stream/sample10/accounts/:account\_name/publishers/twitter/:stream\_label.json?partition=1&backfillMinutes=5  

**NOTES:**

* You do have the option to always use ‘backfillMinutes=5’ when you connect, then handling any duplicate data that is provided.
    
* If you are disconnected for more than five minutes, you can recover data using Recovery.