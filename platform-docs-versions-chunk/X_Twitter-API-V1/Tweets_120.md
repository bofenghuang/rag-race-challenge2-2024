platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/connecting

## Stalls

Set a timer, either a 90 second TCP level socket timeout, or a 90 second application level timer on the receipt of new data. If 90 seconds pass with no data received, including newlines, disconnect and reconnect immediately according to the backoff strategies in the next section. The Streaming API will send a keep-alive newline every 30 seconds to prevent your application from timing out the connection. You should wait at least 3 cycles to prevent spurious reconnects in the event of network congestion, local CPU starvation, local GC pauses, etc.