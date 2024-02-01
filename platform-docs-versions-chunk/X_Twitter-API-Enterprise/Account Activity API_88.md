platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

## DELETE account\_activity/webhooks/:webhook\_id/subscriptions/all (DEPRECATED)[¶](#delete-account-activity-webhooks-webhook-id-subscriptions-all-deprecated- "Permalink to this headline")

Deactivates subscription(s) for the provided user context and application. After deactivation, all events for the requesting user will no longer be sent to the webhook URL.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (3-legged OAuth - Whitelisted consumer key and subscribed user's access token) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 500 |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |