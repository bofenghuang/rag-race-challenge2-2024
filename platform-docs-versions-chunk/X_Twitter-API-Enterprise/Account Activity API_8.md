platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/quick-start/enterprise-account-activity-api


### Managing subscribed users:

  
Once you've registered a Webhook, you can add a subscribed user to the Account Activity API to begin receiving their account activities.

* [Adding a subscription](#tab1)
* [Viewing subscriptions](#tab2)
* [Removing a subscription](#tab3)
* [](#tab4)

Adding a subscription

Viewing subscriptions

Removing a subscription

We'll begin with subscribing a user so you recieve all event types.

Copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`  
    
* **Consumer key name** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`  
    
* **Subscribing user's access token** `<SUBSCRIBING_USER'S_ACCESS_TOKEN>` e.g. `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`  
    

      `curl --request POST --url https://api.twitter.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>/subscriptions/all.json --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<SUBSCRIBING_USER'S_ACCESS_TOKEN>", oauth_version="1.0"'`
    

To view a list of all activity type subscriptions for a specified webhook, copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`  
    
* **Bearer token** `<BEARER_TOKEN>` e.g. `AAAAAAAAAAAA0%2EUifi76ZC9Ub0wn...`  
    

      `curl --request GET --url https://api.twitter.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>/subscriptions/all/list.json --header 'authorization: Bearer <BEARER_TOKEN>'`
    

After deactivation, all events for the requesting user will no longer be sent to the webhook URL.  

To deactivate a subscription from the provided user context and application, copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`  
    
* **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`  
    
* **Subscribing user's access token** `<SUBSCRIBING_USER'S_ACCESS_TOKEN>` e.g. `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`  
    

      `curl --request DELETE --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBED_USER'S_ACCESS_TOKEN", oauth_version="1.0"'`
    

Great job! You should now able to manage your webhooks and subscribed users.