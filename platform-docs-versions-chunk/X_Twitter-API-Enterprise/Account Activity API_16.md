platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks


### 3\. Develop webhook consumer app

Once you have received Account Activity API access, you need to develop, deploy and host a web app that will receive Twitter webhook events. 

* Create a web app with a URL to use as your webhook to receive events. This is the endpoint deployed on your server to listen for incoming Twitter webhook events. 
    * The URI _path_ is completely up to you. This example would be valid: https://mydomain.com_/service/listen_  
        
    * If you are listening for webhooks from a variety of sources, a common pattern is: https://mydomain.com/webhook/twitter
    * Note that the specified URL can not include a port specification (https://mydomain.com:5000/NoWorkie).
* As described in our [Securing Webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks) guide, a first step is writing code that receives a Twitter Challenge Response Check (CRC) GET request and responds with a properly formatted JSON response. 
* Register your webhook URL. You will make a POST request to a /webhooks.json?url= endpoint. When you make this request Twitter will issue a CRC request to your web app. When a webhook is successfully registered, the response will include a webhook id. This webhook id is needed later when making some requests to the Account Activity API.   
    
* Twitter will send account webhook events to the URL you registered. Make sure your web app supports POST requests for incoming events. These events will be encoded in JSON. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects) for example webhook JSON payloads.
* Once your web app is ready, the next step is adding accounts to receive activities for. When adding (or deleting) accounts you will make POST requests referencing the account id. See our [guide on adding subscriptions](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/managing-webhooks-and-subscriptions) for more information.