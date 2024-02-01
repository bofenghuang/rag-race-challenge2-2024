platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-list

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. **Note:** : Specifies the ID of the user to get lists from. Helpful for disambiguating when a valid user ID is also a valid screen name. |     | _12345_ |
| screen\_name | optional | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     | _noradio_ |
| reverse | optional | Set this to _true_ if you would like owned lists to be returned first. See description above for information on how this parameter works. |     | _true_ |

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/lists/list.json?screen_name=twitterapi`