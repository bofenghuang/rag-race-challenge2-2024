platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### HTTP Response Codes[¶](#http-response-codes "Permalink to this headline")

| Code | Message |
| --- | --- |
| 200 | Success. A list of subscriptions for the requested webhook will be returned. |
| 401 | Your application does not have permission to view subscriptions for the specified webhook. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request GET 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all/list.json 
     --header 'authorization: Bearer TOKEN'

### Example Response - Success[¶](#example-response-success "Permalink to this headline")

_HTTP 200_

    {
      "webhook_id": "1234567890",
      "webhook_url": "https://your_domain.com/webhook/twitter/0",
      "application_id": "11231812",
      "subscriptions": [{
        "user_id": "20212306"
      }]
    }