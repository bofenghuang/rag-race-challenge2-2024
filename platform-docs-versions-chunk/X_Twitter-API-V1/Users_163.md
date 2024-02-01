platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-destroy

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/lists/destroy.json?owner_screen_name=kurrik&slug=goonies`