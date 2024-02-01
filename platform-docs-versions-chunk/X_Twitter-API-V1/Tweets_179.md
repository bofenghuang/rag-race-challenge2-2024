platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-remove

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the target Collection. |     | _custom-388061495298244609_ |
| tweet\_id | required | The identifier of the Tweet to remove. |     | _390839888012382208_ |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/collections/entries/remove.json?id=custom-388061495298244609&tweet_id=390890231215292416`