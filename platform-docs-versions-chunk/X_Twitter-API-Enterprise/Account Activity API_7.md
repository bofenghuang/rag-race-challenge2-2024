platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/quick-start/enterprise-account-activity-api


### Managing a webhook:

  
Using a webhook provides you the ability to subscribe to realtime activities related to a user account through a single connection. 

* [Adding a webhook](#tab1)
* [Viewing a webhook](#tab2)
* [Removing a webhook](#tab3)
* [](#tab4)

Adding a webhook

Viewing a webhook

Removing a webhook

Let’s begin with registering a new webhook URL for the given application context.

The URL will be validated via a CRC request before saving. Once you've registered a webhook, make sure to document the webhook ID as you will need it later on.

Copy the following cURL request into your command line after making changes to the following:

* **URL** `<URL>` e.g. `https://yourdomain.com/webhooks/twitter/`  
    
* **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`  
    
* **Access token** `<ACCESS_TOKEN>` e.g.  `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

      `curl --request POST --url 'https://api.twitter.com/1.1/account_activity/webhooks.json?url=<URL>' --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<ACCESS_TOKEN>", oauth_version="1.0"'`
    

We will run the following command to returns all registered webhook URLs and their statuses for the given application.

Copy the following cURL request into your command line after making changes to the following:

* **Bearer token** `<BEARER_TOKEN>` e.g. `AAAAAAAAAAAA0%2EUifi76ZC9Ub0wn...`

      `curl --request GET --url https://api.twitter.com/1.1/account_activity/webhooks.json --header 'authorization: Bearer <BEARER_TOKEN>'`
    

To remove a webhook from the provided application's configuration, copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`  
    
* **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`  
    
* **Access token** `<ACCESS_TOKEN>` e.g.  `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

      `curl --request DELETE --url https://api.twitter.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>.json --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<ACCESS_TOKEN>", oauth_version="1.0"'`