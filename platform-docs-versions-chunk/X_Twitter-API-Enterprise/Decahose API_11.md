platform: X
topic: Twitter-API-Enterprise
subtopic: Decahose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Decahose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/guides/recovery-and-redundancy

## Additional Streams

Having additional Decahose streams is another way to help build reliability into your solution. Any additional streams are completely independent, having their unique endpoint. Each stream is assigned its own stream\_label, and this label, along with your account name, are part of that stream’s URL. See the example below:

https://gnip-stream.twitter.com/stream/sample10/accounts/:account\_name/publishers/twitter/:stream\_label.json

The most common convention is to have a realtime stream dedicated for you production system, and an additional stream available for development and testing. Having a test/development stream enables Decahose customers to have a stream to test client consumer updates. While any (unique) label can be assigned to a stream, one convention is to use ‘prod’ for production stream, and ‘dev’ or ‘sandbox’ for an additional development stream.

The number of streams, and their unique labels, is configurable by your account representative.