platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features

## Redundant connections 

A redundant connection simply allows you to establish more than 1 simultaneous connections to the data stream. This provides redundancy by allowing you to connect to the same stream with two separate consumers, receiving the same data through both connections. Thus, your app has a hot failover for various situations, e.g. where one stream is disconnected or where your app’s primary server fails.

The number of connections allowed for any given stream is configurable by your account representative. To use a redundant stream, simply connect to the same URL used for your primary connection. The data for your stream will be sent through both connections, with both stream connections represented on the stream dashboard.

Note that for billing purposes, we deduplicate the activity counts you receive through multiple connections such that you are only billed for each unique activity once.