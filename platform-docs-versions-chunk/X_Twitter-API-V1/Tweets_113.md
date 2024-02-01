platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/streaming-message-types

###   
Stall warnings (warning)

When connected to a stream using the stall\_warnings parameter, you may receive status notices indicating the current health of the connection. See the [stall\_warnings](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/basic-operators.html) documentation for more information.

{  
"warning":{  
"code":"FALLING\_BEHIND",  
"message":"Your connection is falling behind and messages are being queued for delivery to you. Your queue is now over 60% full. You will be disconnected when the queue is full.",  
"percent\_full": 60  
}  
}

### Compliance Messages