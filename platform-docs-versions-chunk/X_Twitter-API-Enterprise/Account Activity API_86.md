platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 32  | Could not authenticate you. |

_HTTP 401_

    {
      "errors": [
        {
           "code": 32,
          "message": "Could not authenticate you."
        }
      ]
    }

## DELETE account\_activity/webhooks/:webhook\_id[¶](#delete-account-activity-webhooks-webhook-id "Permalink to this headline")

Removes the webhook from the provided application's configuration. The webhook ID can be accessed by making a call to GET /1.1/account\_activity/webhooks.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (user context - all consumer and access tokens) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 15  |