platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

## GET account\_activity/webhooks/:webhook\_id/subscriptions/all/list[¶](#get-account-activity-webhooks-webhook-id-subscriptions-all-list "Permalink to this headline")

Returns a list of the current All Activity type subscriptions for the specified webhook. Note that the /list endpoint requires application-only OAuth, so requests should be made using a bearer token instead of user context.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all/list.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | HTTP response code |
| Requires Authentication | Yes (application only - bearer token) |
| Rate Limited | Yes |
| Requests / 15-min window (application auth) | 50  |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |