platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters


### count

This parameter requires elevated access to use.

When reconnecting to a streaming endpoint, elevated access clients may include the count parameter to attempt to backfill missed messages which occurred during the disconnect period. The supplied value may be an integer from 1 to 150000 or from -1 to -150000. If a positive number is specified, the stream will transition to live values once the backfill has been delivered to the client. If a negative number is specified, the stream will disconnect once the backfill has been delivered to the client, which may be useful for debugging.

Note that use of this parameter should be carefully considered, as high values increase the chance of a subsequent disconnect. To demonstrate this, consider the case where a client connects without backfill. Upon establishing a connection, Twitter will allocate a fixed-size queue, and begin adding messages to be streamed to the client. If the client reads too slowly, the queue will fill up. Once full, Twitter will disconnect the client:

When a client connects with backfill, that number of messages are immediately added to the queue. The client must read messages faster than the current rate of Tweets being added to the queue, as the available buffer before a disconnect occurs can be much smaller than when connecting without backfill.