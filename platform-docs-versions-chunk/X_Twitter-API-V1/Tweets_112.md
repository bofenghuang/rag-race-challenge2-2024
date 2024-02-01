platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/streaming-message-types


### Disconnect messages (disconnect)

Streams may be shut down for a variety of reasons. The streaming API will attempt to deliver a message indicating why a stream was closed. Note that if the disconnect was due to network issues or a client reading too slowly, it is possible that this message will not be received.

{  
"disconnect":{  
"code": 4,  
"stream\_name":"",  
"reason":""  
}  
}

The following table lists possible status codes and their meanings. Additional codes may be used without warning.

| Code | Name | Description |
| --- | --- | --- |
| 1   | Shutdown | The feed was shutdown (possibly a machine restart) |
| 2   | Duplicate stream | The same endpoint was connected too many times. |
| 4   | Stall | The client was reading too slowly and was disconnected by the server. |
| 5   | Normal | The client appeared to have initiated a disconnect. |
| 7   | Admin logout | The same credentials were used to connect a new stream and the oldest was disconnected. |
| 9   | Max message limit | The stream connected with a negative count parameter and was disconnected after all backfill was delivered. |
| 10  | Stream exception | An internal issue disconnected the stream. |
| 11  | Broker stall | An internal issue disconnected the stream. |
| 12  | Shed load | The host the stream was connected to became overloaded and streams were disconnected to balance load. Reconnect as usual. |