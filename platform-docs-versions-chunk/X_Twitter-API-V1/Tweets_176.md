platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-move

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the Collection receiving the Tweet. |     | _custom-388061495298244609_ |
| tweet\_id | required | The identifier of the Tweet to add to the Collection. |     | _390839888012382208_ |
| relative\_to | required | The identifier of the Tweet used for relative positioning. |     | _614929127313965056_ |
| above | optional | Set to _false_ to insert the specified _tweet\_id_ below the _relative\_to_ Tweet in the collection. Default: _true_ |     | _false_ |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/collections/entries/move.json?id=custom-388061495298244609&tweet_id=390839888012382208&relative_to=614929127313965056`

## Example Response[¶](#example-response "Permalink to this headline")