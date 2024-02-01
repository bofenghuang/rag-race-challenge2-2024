platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide


### **Follow the steps below to easily migrate from the Site Streams API to the Account Activity API**

**Step 1: Decide on a Package**

Depending on how you are currently operating with User Streams or Site Streams, you should consider moving to either the enterprise or premium version of the Account Activity API.  Consider the number of applications or authorized users you are currently supporting and scale appropriately to the volume and reliability needed.  When deciding on the package that best suits your needs, some things worth considering are:

* Number of webhooks needed
* Current/projected subscriptions/authorized users managed on your application
* Current number of Twitter client applications
* The level of support you'd prefer from Twitter (forum support or managed enterprise level 1:1 support)
* Price of each package

**Step 2:** **Check the Setup of your Twitter app in the developer portal**

The [Twitter app](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps) currently used for User Streams or Site Streams will be listed for the owning user within the [developer portal](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/overview). This Twitter app can also be used for Account Activity API to retain authorized users for that application.  A new app can also be created, and users can be re-authorized for this new app if desired.  If you are creating a new app on behalf of a business, it is recommended that you create the app with a corporate Twitter @handle account.

* Enable “Read, Write and Access direct messages” on the [permissions](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-permission-model) tab of your Twitter app page.   
    \*Note that changing these settings is not retroactive, any authorized users will keep the authorization settings from the time at which they were authorized. If a user has not already given you read, write and direct message access, you will need to have that user re-authorize your application.
* If you are unfamiliar with [Twitter Sign-in](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/guides/log-in-with-twitter) and how user contexts work with the Twitter API review [Obtaining Access Tokens](https://dev.twitter.com/webhooks/access-tokens).
* Generate access tokens for the Twitter app owner at the bottom of the “Keys and Tokens” tab. On this same tab take note of your Consumer Key, Consumer Secret, Access Token and Access Token Secret. You will need these to use the API.
* Generate a bearer token using your Consumer Key and Consumer Secret for [application-only](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-only) API methods.

**Step 3: Setup & Configure Your Webhooks**

* Create a web app with an endpoint to use as your webhook to receive events (e.g. https://your\_domain.com/webhook/twitter or https://webhooks.your\_domain.com).
* Use your Consumer Key, Consumer Secret, Access Token and Access Token Secret when creating your webhook, Note that your endpoint must return a JSON response with a response\_token that is a base64 encoded HMAC SHA-256 hash created from the crc\_token and your app Consumer Secret.  
    
* Review [Securing Webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks) documentation taking special note of the Challenge Response Check (CRC) requirements.
* Make sure your webhook supports POST requests for incoming events and GET requests for the CRC.
* Make sure your webhook has low latency (<3 seconds to respond to POST requests)

**Step 4: Validate Your Webhook Setup**

* Webhook APIs will secure your webhooks in two ways:

               - Require challenge response checks to validate that the webhook owner is the web app owner.

               - A signature header in each POST request for your web app to validate the source.

* In order to verify that you are both the owner of the web app and the webhook URL, Twitter will perform a Challenge Response Check (CRC), which is not to be confused with a cyclic redundancy check.
* A GET request with a parameter named crc\_token will be sent to your webhook URL. Your endpoint must return a JSON response with a response\_token that is a base64 encoded HMAC SHA-256 hash created from the crc\_token and your app Consumer Secret.
* The crc\_token should be expected to change for each incoming CRC request. The crc\_token should be used as the message in the calculation, where your Consumer Secret is the key.
* In the event that the response is invalid, events will cease to be sent to the registered webhook.

**Step 5: Create Subscriptions for Each User Stream or Site Streams Authorized User**

Converting to the Account Activity API from User Streams:

* Generate a list of your current user subscriptions on User Streams
* Set up your new Account Activity API subscriptions using the request:  _POST account\_activity/all/:env\_name/subscriptions_
* Confirm your Account Activity API subscriptions using the request:  _GET account\_activity/all/:env\_name/subscriptions/list_ 

Converting to the Account Activity API from Site Streams: (using control streams):

* Generate a list of your current subscriptions on Site Streams using the request:  _GET /1.1/site/c/:stream\_id/info.json_
* Set up your new Account Activity API subscriptions using the request:  _POST account\_activity/all/:env\_name/subscriptions_
* Confirm your Account Activity API subscriptions using the request:  _GET account\_activity/all/:env\_name/subscriptions/list_ 

Registering a Webhook and Creating Subscriptions (not migrating from Site Streams or User Streams)

* Register your webhook URL with your app using [POST webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks) and receive a webhook\_id.
* Use the returned webhook\_id to add user subscriptions with [POST webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks-webhook-id-subscriptions-all).