platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters

### replies (deprecated)

Available on User Streams and Site Streams (deprectated)  

By default @replies are only sent if the current user follows both the sender and receiver of the reply. For example, consider the case where Alice follows Bob, but Alice doesn’t follow Carol. By default, if Bob @replies Carol, Alice does not see the Tweet. This mimics twitter.com and api.twitter.com behavior. To have such Tweets returned in a streaming connection, specify replies=all when connecting.