platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/get-collections-entries

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the Collection for which to return results. |     | _custom-539487832448843776_ |
| count | optional | Specifies the _maximum_ number of results to include in the response. Specify a count between 1 and 200. A _next\_cursor_ value will be provided in the response if additional results are available. |     | _100_ |
| max\_position | optional | Returns results with a position value less than or equal to the specified position. |     | _54321_ |
| min\_position | optional | Returns results with a position greater than the specified position. |     | _12345_ |

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/collections/entries.json?id=custom-539487832448843776`