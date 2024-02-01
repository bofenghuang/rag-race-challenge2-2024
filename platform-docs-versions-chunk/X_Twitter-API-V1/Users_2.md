platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/get-account-settings

GET account/settings

get-account-settings

# GET account/settings

Returns settings (including current trend, geo and sleep time information) for the authenticating user.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account/settings.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

## Parameters[¶](#parameters "Permalink to this headline")

None

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/account/settings.json`