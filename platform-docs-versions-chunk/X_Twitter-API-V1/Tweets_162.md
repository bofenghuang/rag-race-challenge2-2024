platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/get-collections-show

GET collections/show

get-collections-show

# GET collections/show

Retrieve information associated with a specific Collection.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/collections/show.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 1000 |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the Collection for which to return results. |     | _custom-388061495298244609_ |

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/collections/show.json?id=custom-393773266801659904`