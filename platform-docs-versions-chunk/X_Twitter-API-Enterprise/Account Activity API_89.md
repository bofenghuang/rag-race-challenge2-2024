platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request DELETE 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
     --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBED_USER'S_ACCESS_TOKEN", oauth_version="1.0"'
    
    Example Request

* * *

    { }

## DELETE /account\_activity/webhooks/:webhook\_id/subscriptions/:user\_id/all.json[¶](#delete-account-activity-webhooks-webhook-id-subscriptions-user-id-all-json "Permalink to this headline")

Deactivates subscription for the specified webhook and user id. After deactivation, all events for the requesting user will no longer be sent to the webhook URL. Note, that this endpoint requires application-only OAuth, so requests should be made using a bearer token instead of user context.