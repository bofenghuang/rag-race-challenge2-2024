platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/streaming-message-types

## Standard stream messages

In addition to [standard Tweet payloads](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html), the following kinds of messages may be delivered on a stream. Note that this list may not be comprehensive—additional objects may be introduced into streams. Ensure that your parser is tolerant of unexpected message formats.

When parsing Tweets, keep in mind that Retweets are streamed as a status with another status nested inside it. If you are matching Tweet fields using regular expressions, it is possible that you will match fields in the nested Tweet instead of the wrapper. As a rule of thumb it is better to use a JSON parser to extract information from message payloads.

### Maintenance Messages

### Blank lines

On slow streams, some messages may be blank lines (\\r\\n or similar) which serve as “keep-alive” signals to prevent clients and other network infrastructure from assuming the stream has stalled and closing the connection.