platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters

### follow

A comma-separated list of user IDs, indicating the users whose Tweets should be delivered on the stream. Following protected users is not supported. For each user specified, the stream will contain:

* Tweets created by the user.
* Tweets which are retweeted by the user.
* Replies to any Tweet created by the user.
* Retweets of any Tweet created by the user.
* Manual replies, created without pressing a reply button (e.g. “@twitterapi I agree”).

The stream will not contain:

* Tweets mentioning the user (e.g. “Hello @twitterapi!”).
* Manual Retweets created without pressing a Retweet button (e.g. “RT @twitterapi The API is great”).
* Tweets by protected users.