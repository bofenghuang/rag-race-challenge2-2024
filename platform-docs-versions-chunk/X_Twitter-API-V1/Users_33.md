platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-saved_searches-destroy-id

POST saved\_searches/destroy/:id

post-saved\_searches-destroy-id

# POST saved\_searches/destroy/:id

Destroys a saved search for the authenticating user. The authenticating user must be the owner of saved search id being destroyed.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/saved_searches/destroy/:id.json`

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
| id  | required | The ID of the saved search. |     | _313006_ |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/saved_searches/destroy/62353170.json`