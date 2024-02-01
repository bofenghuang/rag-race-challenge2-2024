platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (application only - bearer token) |
| Rate Limited | Yes |
| Requests / 15-min window (application auth) | 15  |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request GET 
     --url https://api.twitter.com/1.1/account_activity/webhooks.json 
     --header 'authorization: Bearer TOKEN'