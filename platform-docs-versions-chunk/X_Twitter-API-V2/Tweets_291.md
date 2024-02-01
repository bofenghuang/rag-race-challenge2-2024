platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/integrate/consuming-sampled-stream-data


## Consuming sampled stream data

Consuming data from the sampled stream is very similar to the filtered stream integration recommendations.  For understanding how to consume from a streaming endpoint, please follow the recommendations given in the consuming streaming data integration guide, and note the following differences with sampled stream.

* Although only 1% of Tweets, the volume of the sampled stream can be very high, and your client should have a high volume capacity.
* Tweets delivered through the sampled stream endpoint do not count towards the monthly total Tweet volume.
* Tweets delivered with sampled stream will not have a matching rules object.  
     

**Best Practices**

When consuming realtime data, maximizing your connection time is a fundamental goal to promote both data reliability and data full-fidelity. When disconnects occur, it is important for your client to automatically detect the disconnection, [handle the disconnection](https://developer.twitter.com/en/docs/twitter-api/tweets/sampled-stream/integrate/handling-disconnections) and reconnect quickly.