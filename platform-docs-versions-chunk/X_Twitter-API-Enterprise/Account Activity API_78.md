platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request POST 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
     --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBING_USER'S_ACCESS_TOKEN", oauth_version="1.0"'

### Example Response - Success[¶](#example-response-success "Permalink to this headline")

_HTTP 204 NO CONTENT_

    {}