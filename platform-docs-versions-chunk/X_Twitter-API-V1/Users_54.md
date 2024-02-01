platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-blocks-destroy

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the potentially blocked user. Helpful for disambiguating when a valid screen name is also a user ID. |     | _noradio_ |
| user\_id | optional | The ID of the potentially blocked user. Helpful for disambiguating when a valid user ID is also a valid screen name. |     | _12345_ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_ . |     | _false_ |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user objects. |     |     |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/blocks/destroy.json?screen_name=theSeanCook&skip_status=1`