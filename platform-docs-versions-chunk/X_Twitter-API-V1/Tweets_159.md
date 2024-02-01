platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/get-collections-list

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | required | The ID of the user for whom to return results. |     | _20_ |
| screen\_name | required | The screen name of the user for whom to return results. |     | _twitterdev_ |
| tweet\_id | optional | The identifier of the Tweet for which to return results. |     | _514533751213551616_ |
| count | optional | Specifies the _maximum_ number of results to include in the response. Specify a count between 1 and 200. A _next\_cursor_ value will be provided in the response if additional results are available. |     | _100_ |
| cursor | optional | A string identifying the segment of the current result set to retrieve. Values for this parameter are yielded in the _cursors_ node attached to response objects. Usage of the _count_ parameter affects cursoring. |     | _BXb2synCEAE_ |