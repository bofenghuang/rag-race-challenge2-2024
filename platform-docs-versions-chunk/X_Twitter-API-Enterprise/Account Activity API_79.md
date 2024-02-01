platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 34  | Webhook does not exist or is associated with a different twitter application. |
| 348 | Client application is not permitted to access this user's webhook subscriptions. |

## GET account\_activity/subscriptions/count[¶](#get-account-activity-subscriptions-count "Permalink to this headline")

Returns the count of subscriptions that are currently active on your account. Note that the /count endpoint requires application-only OAuth, so that you should make requests using a bearer token instead of user context.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/subscriptions/count.json`