platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-update

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the Collection to modify. |     | _custom-388061495298244609_ |
| name | optional | The title of the Collection being created, in 25 characters or fewer. |     | _Sweet%20Tweets_ |
| description | optional | A brief description of this Collection in 160 characters or fewer. |     | _My%20favorite%20tweets%20ever_ |
| url | optional | A fully-qualified URL to associate with this Collection. |     | `https%3A%2F%2Fexample.com%2F` |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/collections/update.json?name=Subtweets&id=custom-390882285743898624`