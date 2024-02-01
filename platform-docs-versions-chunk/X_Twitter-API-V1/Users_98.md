platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-show

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| source\_id | optional | The user\_id of the subject user. |     | _783214_ |
| source\_screen\_name | optional | The screen\_name of the subject user. |     | _Twitter_ |
| target\_id | optional | The user\_id of the target user. |     | _2244994945_ |
| target\_screen\_name | optional | The screen\_name of the target user. |     | _TwitterDev_ |

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/friendships/show.json?source_screen_name=twitterdev&target_screen_name=twitter`