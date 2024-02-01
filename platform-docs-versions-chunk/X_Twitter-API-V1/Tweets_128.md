platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters

### delimited

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this to the string length indicates that statuses should be delimited in the stream, so that clients know how many bytes to read before the end of the status message. Statuses are represented by a length, in bytes, a newline, and the status text that is exactly length bytes. Note that “keep-alive” newlines may be inserted before each length.

As an example, consider this response to a request to https://stream.twitter.com/1.1/statuses/filter.json?delimited=length&track=twitterapi:

The 1953 indicates how many bytes to read off of the stream to get the rest of the Tweet (including rn). The next length delimiter will occur exactly after 1953 bytes.