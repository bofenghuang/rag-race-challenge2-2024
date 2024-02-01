platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features


## Additional streams 

Having additional PowerTrack streams is another way to help build reliability into your solution. So much so that it is considered a best practice. Any additional streams are completely independent, having their unique endpoint and independent rule set. Each stream is assigned its own ‘label’, and this label, along with your account name, are part of that stream’s URL.

https://gnip-stream.twitter.com/stream/powertrack/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json  

The most common convention is to have a realtime stream dedicated for your production system, and an additional stream available for development and testing. Having a test/development stream enables PowerTrack customers to have a stream to test client consumer updates. While any (unique) label can be assigned to a stream, one convention is to use ‘prod’ for production stream, and ‘dev’ or ‘sandbox’ for an additional development stream.

The number of streams, and their unique labels, is configurable by your account representative.