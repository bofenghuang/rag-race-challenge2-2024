platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the potentially muted user. Helpful for disambiguating when a valid screen name is also a user ID. |     | _whiteleaf_ |
| user\_id | optional | The ID of the potentially muted user. Helpful for disambiguating when a valid user ID is also a valid screen name. |     | _12345_ |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/mutes/users/destroy.json?screen_name=evilpiper`