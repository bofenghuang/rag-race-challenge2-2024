platform: X
topic: Twitter-API-Enterprise
subtopic: Decahose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Decahose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/guides/recovery-and-redundancy


## Redundant Connections 

A redundant connection simply allows you to establish more than one simultaneous connection to the data stream. This provides redundancy by allowing you to connect to the same stream with two separate consumers, receiving the same data through both connections. Thus, your app has a hot failover for various situations, e.g. where one stream is disconnected or where your app’s primary server fails.

The number of connections allowed for any given stream is configurable by your account representative. To use a redundant stream, simply connect to the same URL used for your primary connection. The data for your stream will be sent through both connections, with both stream connections represented on the stream dashboard.

Note that for billing purposes, we deduplicate the activity counts you receive through multiple connections such that you are only billed for each unique activity once. Given the Decahose has two partitions, here's an example of how the connection count works below:

Connect to decahose partition=1  
Connect to decahose partition=1  
Connect to decahose partition=2

The above situation yields a total of three connections – two connections to partition=1 and one connection to partition=2. Normally, you would want the same number of connections to each partition, so this example highlights a situation where the redundant connection to partition=2 has dropped and you want to further invstigate.