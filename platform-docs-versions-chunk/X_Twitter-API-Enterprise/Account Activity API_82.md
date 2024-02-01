platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

## GET account\_activity/webhooks/:webhook\_id/subscriptions/all[¶](#get-account-activity-webhooks-webhook-id-subscriptions-all "Permalink to this headline")

Provides a way to determine if a webhook configuration is subscribed to the provided user’s events. If the provided user context has an active subscription with provided application, returns 204 OK. If the response code is not 204, then the user does not have an active subscription. See HTTP Response code and error messages below for details.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (3-legged OAuth - Whitelisted consumer key and subscribing user's access token) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 500 |