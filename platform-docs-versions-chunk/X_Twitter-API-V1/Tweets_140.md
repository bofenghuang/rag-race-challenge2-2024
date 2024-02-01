platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/api-reference/post-statuses-filter


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |
| --- | --- | --- |
| Name | Required | Description |
| follow | optional | A comma separated list of user IDs, indicating the users to return statuses for in the stream. See [follow](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information. |
| track | optional | Keywords to track. Phrases of keywords are specified by a comma-separated list. See [track](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information. |
| locations | optional | Specifies a set of bounding boxes to track. See [locations](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information. |
| delimited | optional | Specifies whether messages should be length-delimited. See [delimited](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information. |
| stall\_warnings | optional | Specifies whether stall warnings should be delivered. See [stall\_warnings](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information. |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object. |