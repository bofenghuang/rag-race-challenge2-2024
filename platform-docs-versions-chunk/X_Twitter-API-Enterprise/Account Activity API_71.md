platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request POST 
       --url 'https://api.twitter.com/1.1/account_activity/webhooks.json?url=https%3A%2F%2Fyour_domain.com%2Fwebhooks%2Ftwitter%2F0' 
       --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'

### HTTP Responses[¶](#http-responses "Permalink to this headline")

| HTTP Code | Message |
| --- | --- |
| 200 | Webhook URL is registered to the provided application |
| 403 | There is an error with your request. See error messages section below. |

### Example Response - Success[¶](#example-response-success "Permalink to this headline")

_HTTP 200_

    {
      "id": "1234567890",
      "url": "https://your_domain.com/webhook/twitter/0",
      "valid": true,
      "created_at": "2016-06-02T23:54:02Z"
    }