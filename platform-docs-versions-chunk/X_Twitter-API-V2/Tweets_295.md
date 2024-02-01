platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/integrate/handling-disconnections


### Rate limits and usage

To check connection limits response will return three headers. This is useful to understand how many reconnections attempts are allowed for the streaming endpoint.

* x-rate-limit-limit indicates the number of allotted requests your client is allowed to make during the 15-minute window.
    
* x-rate-limit-remaining indicates the number of requests made so far in the 15-minute window.
    
* x-rate-limit-reset is a UNIX timestamp indicating when the 15-minute window will restart, resetting x-rate-limit-remaining to 0.
    

The sampled stream endpoint does not currently report usage data. To check how many Tweets have been delivered, your code can implement a metering logic, so that consumption can be measured and paused if needed. 

Your code that hosts the client side of the stream simply inserts incoming Tweets into a first in, first out (FIFO) queue, or a similar memory structure; a separate process/thread should consume Tweets from that queue to parse and prepare content for storage. With this design, you can implement a service that can scale efficiently in case incoming Tweet volumes changes dramatically. Conceptually, you can think of it as downloading an infinitely long file over HTTP.