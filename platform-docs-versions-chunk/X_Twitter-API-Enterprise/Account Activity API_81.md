platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Example Response - Success[¶](#example-response-success "Permalink to this headline")

_HTTP 200_

    {
      "account_name":"my-account",
      "subscriptions_count_all":"1",
      "subscriptions_count_direct_messages":"0",
      "provisioned_count":"50"
    }

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