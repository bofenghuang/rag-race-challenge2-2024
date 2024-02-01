platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters

### with (deprecated)

Available on User Streams and Site Streams (deprecated)

The with parameter controls the types of messages delivered to User and Site Streams clients.

* The default for Site Streams is with=user, which only streams messages from the user associated with the stream.
* The default for User Streams is with=followings which adds messages from accounts the user follows, equivalent to the user’s home timeline.

Despite the difference in defaults, Site and User each accept both user and followings parameter values.