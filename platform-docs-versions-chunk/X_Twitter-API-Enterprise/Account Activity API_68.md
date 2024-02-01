platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/faq


### Error troubleshooting guide

#### Code 32

This error generally means that something is either malformed in the request, headers, authorization, or url that you are specifying. This is not an Account Activity API error, it’s an authorization error and Twitter isn’t getting the proper Oauth setup or url.

* **Enterprise** - Make sure the consumer keys and access tokens you are using belong to a [Twitter app](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps) that has been registered for use of Enterprise products. If you don't have your consumer keys and access tokens, or need to add your Twitter app to the allowlist, please reach out to your account manager.   
    
* If authenticating with user context, make sure you have properly [authorized your request](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/guides/authorizing-a-request) with the proper `oauth nonce`, `oauth_signature`, and `oauth_timestamp`.  
    
* Make sure that your access tokens have the proper permission level.
    * When on the 'Keys and tokens' tab in the [app dashboard](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps), please make sure that your access tokens have the 'Read, write, and direct messages' [permission level](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-permission-model). 
    * If the tokens' permission level is set to anything less than this, please navigate to the 'Permissions' tab, adjust the access permission to 'Read, write, and direct messages', then regenerate your access tokens and secret from the 'Keys and tokens' tab.

* Make sure that your URL is formed properly.
    * Please keep in mind that `:env_name` is case sensitive.  
         

#### Code 200 - Forbidden

* **Premium** - Make sure that you have an approved [developer account](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/overview) before you try to make a request to the API. You also must use the proper :env\_name in the request, which you can setup on the [dev environments](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/dev-environments) page.  
    
* **Enterprise** - Make sure that your account manager has set you up with access to the Account Activity API.
* Make sure you have set up your URI properly. This error can trigger if you have entered the incorrect URI in your request.  
     

#### Code 214 - Webhook URL does not meet the requirements.

* Please make sure that you are using https.
* Your webhook URL could be malformed.
* Learn more about how to set up your webhook URL under the [Develop webhook consumer app](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks#webhook-url) section on [Getting started with webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks) page.  
     

#### Code 214 - High latency on CRC GET request. Your webhook should respond in less than 3 seconds.

* This means that your server is slow. Make sure that you are responding to the CRC within 3 seconds.  
     

#### Code 214 - Non-200 response code during CRC GET request (i.e. 404, 500, etc).

* Your server is down. Make sure that your server is running properly.  
     

#### Code 214 - Too many resources already created.

* **Enterprise** - You have already used all of your webhooks. Use the [GET webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks) endpoint with each of your registered apps to identify where your webhooks are distributed.   
      
    

#### Code 261 - Application cannot perform write actions.

* The app that you are using with the API does not have the proper [permission level](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-permission-model) set for its access token and access token secret. Please navigate to the 'Keys and tokens' tab on the [Twitter apps](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps) dashboard and check the permission levels assigned to your access token and access token secret. If it is set to anything other than 'Read, write and Direct Messages,' then you are going to have to adjust the settings under the 'Permission' tab and regenerate your access token and access token secret to apply the new settings.
* Alternatively, you are trying to register a webhook using app-only authentication, which is not supported. Please authenticate with user context instead as noted in the API reference sections for registering a webhook for [Enterprise Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks).