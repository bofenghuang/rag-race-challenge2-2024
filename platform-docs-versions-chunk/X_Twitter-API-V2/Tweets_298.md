platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/integrate/recovery-and-redundancy-features

### Redundant connections

A redundant connection simply allows you to establish more than one simultaneous connections to sampled stream. This provides redundancy by allowing you to connect to the same stream with two separate consumers, receiving the same data through both connections. Thus, your app has a hot failover for various situations such as if one stream is disconnected or if your application's primary server fails.

Sampled stream currently only allows those with [Enterprise Access](https://developer.twitter.com/en/docs/twitter-api/enterprise) to connect to up to two redundant connections. To use a redundant stream, simply connect to the same URL used for your primary connection. The data for your stream will be sent through both connections.