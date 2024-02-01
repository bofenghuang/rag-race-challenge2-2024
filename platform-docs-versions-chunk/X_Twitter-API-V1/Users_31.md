platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-saved_searches-create

POST saved\_searches/create

post-saved\_searches-create

# POST saved\_searches/create

Create a new saved search for the authenticated user. A user may only have 25 saved searches.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/saved_searches/create.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| query | required | The query of the search the user would like to save. |     |     |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/saved_searches/create.json?query=sandwiches`