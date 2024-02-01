platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

## POST account\_activity/webhooks/:webhook\_id/subscriptions/all[¶](#post-account-activity-webhooks-webhook-id-subscriptions-all "Permalink to this headline")

Subscribes the provided application to all events for the provided user context for all message types. After activation, all events for the requesting user will be sent to the application’s webhook via POST request.

Subscriptions are currently limited based on your account configuration. If you have a need to add more subscriptions, please contact your account manager.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (3-legged OAuth - Whitelisted consumer key and subscribing user's access token) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 500 |