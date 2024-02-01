platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-create

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| name | required | The title of the collection being created, in 25 characters or less. |     | _Sweet%20Tweets_ |
| description | optional | A brief description of this collection in 160 characters or fewer. |     | _My%20favorite%20tweets%20ever_ |
| url | optional | A fully-qualified URL to associate with this collection. |     | `https%3A%2F%2Fexample.com%2F` |
| timeline\_order | optional | Order Tweets chronologically or in the order they are added to a Collection. _curation\_reverse\_chron_ - order added (default) _tweet\_chron_ - oldest first _tweet\_reverse\_chron_ - most recent first |     | _tweet\_reverse\_chron_ |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/collections/create.json?name=Tweets%20to%20reply%20to`