platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-create

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| name | required | The name for the list. A list's name must start with a letter and can consist only of 25 or fewer letters, numbers, "-", or "\_" characters. |     |     |
| mode | optional | Whether your list is public or private. Values can be _public_ or _private_ . If no mode is specified the list will be public. |     |     |
| description | optional | The description to give the list. |     |     |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/lists/create.json?name=Goonies&mode=public&description=For%20life`