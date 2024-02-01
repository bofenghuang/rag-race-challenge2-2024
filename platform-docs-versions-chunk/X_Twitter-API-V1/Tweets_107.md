platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/overview


### Standard 'Track' stream messages

In addition to [standard Tweet payloads](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet.html), the following kinds of messages may be delivered on a stream. Note that this list may not be comprehensive—additional objects may be introduced into streams in the future. Ensure that your parser is tolerant of unexpected message formats.

When parsing Tweets, keep in mind that Retweets are streamed as a status with another status nested inside it. If you are matching Tweet fields using regular expressions, it is possible that you will match fields in the nested Tweet instead of the wrapper. As a rule of thumb it is better to use a JSON parser to extract information from message payloads.

#### Maintenance Messages

#### Blank lines

On slow streams, some messages may be blank lines (\\r\\n or similar) which serve as “keep-alive” signals to prevent clients and other network infrastructure from assuming the stream has stalled and closing the connection.

#### Limit notices (limit)

These messages indicate that a filtered stream has matched more Tweets than its current rate limit allows to be delivered. Limit notices contain a total count of the number of undelivered Tweets since the connection was opened, making them useful for tracking counts of track terms, for example. Note that the counts do not specify which filter predicates undelivered messages matched.

{  
"limit":{  
"track":1234  
}  
}

#### Disconnect messages (disconnect)

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

#### Stall warnings (warning)

When connected to a stream using the stall\_warnings parameter, you may receive status notices indicating the current health of the connection. See the [stall\_warnings](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/basic-operators.html) documentation for more information.

{  
"warning":{  
"code":"FALLING\_BEHIND",  
"message":"Your connection is falling behind and messages are being queued for delivery to you. Your queue is now over 60% full. You will be disconnected when the queue is full.",  
"percent\_full": 60  
}  
}