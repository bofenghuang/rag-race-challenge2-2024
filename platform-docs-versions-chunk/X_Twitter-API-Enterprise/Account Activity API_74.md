platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Example Response[¶](#example-response "Permalink to this headline")

_HTTP 200 OK_

    [
      {
        "id": "1234567890",
        "url": "https://your_domain.com/webhook/twitter/0",
        "valid": true,
        "created_at": "2016-06-02T23:54:02Z"
      }
      {
        "id": "2468013579",
        "url": "https://your_domain2.com/webhook/twitter/0",
        "valid": true,
        "created_at": "2016-06-04T22:31:29Z"
      }
    ]

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 99  | You don’t have access to this resource. |

## PUT account\_activity/webhooks/:webhook\_id[¶](#put-account-activity-webhooks-webhook-id "Permalink to this headline")

Triggers the challenge response check (CRC) for the given webhook's URL. If the check is successful, returns 204 and reenables the webhook by setting its status to `valid`.