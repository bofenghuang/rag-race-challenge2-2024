platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (user context - all consumer and access tokens) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 15  |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request PUT 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID.json 
     --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'