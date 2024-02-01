platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-show

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/lists/show.json?slug=team&owner_screen_name=twitter`