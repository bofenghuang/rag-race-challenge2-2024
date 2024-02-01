platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-recent

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `start` | date (ISO 8601) | Start time for the granularity. |
| `end` | date (ISO 8601) | End time for the granularity. |
| `tweet_count` | integer | Count of the volume of Tweets that match the query. |
| `meta` | object | Creation time of the Tweet. |
| `meta.total_tweet_count` | integer | Total count of the Tweets that match the query. |