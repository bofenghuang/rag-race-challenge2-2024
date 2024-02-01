platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/quick-start


### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

#### Load the Twitter API v2 Postman Collection

To load the Twitter API v2 Postman collection into your workspace, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

  
 

#### Authenticate your request

To make a successful request to **lookup** endpoints, you can use either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0), or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). However, with **manage** endpoints, you can only authenticate with OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE.

Regardless, when using Postman, the default authentication keys and tokens will automatically populate in your requests as long as you've set up your environment properly. 

You can do this by selecting the environment named “Twitter API v2” (in the top-right corner of Postman), and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown). These keys include the following:

* API Key (also known as Consumer Key)
* API Secret Key (also known as Consumer Secret)
* OAuth 1.0a user Access Token
* OAuth 1.0a user Access Token Secret
* App only Access Token
* OAuth 2.0 Client Key (only available if you've set up OAuth 2.0 User Authentication settings in your App's settings)
* OAuth 2.0 Client Secret (only available if you've set up OAuth 2.0 User Authentication settings in your App's settings)