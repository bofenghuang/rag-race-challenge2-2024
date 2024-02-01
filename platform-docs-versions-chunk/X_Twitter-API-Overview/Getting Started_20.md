platform: X
topic: Twitter-API-Overview
subtopic: Getting Started
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Overview/Getting Started.md
url: https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api


###   
Step two: Save your App's key and tokens and keep them secure

Once you have access and have created a Project and App, you will be able to find or generate the following credentials within your developer App:

* **[API Key and Secret](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/api-key-and-secret):** Essentially the username and password for your App. You will use these to authenticate requests that require [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), or to generate other tokens such as user Access Tokens or App Access Token.
    
* **[Access Token and Secret](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens):** In general, Access Tokens represent the user that you are making the request on behalf of. The ones that you can generate via the developer portal represent the user that owns the App. You will use these to authenticate requests that require [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a). If you would like to make requests on behalf of another user, you will need to use the 3-legged OAuth flow for them to authorize you. 
    
* **[Client ID and Client Secret](https://developer.twitter.com/content/en/docs/authentication/oauth-2-0/user-access-token):** These credentials are used to obtain a user Access Token with OAuth 2.0 authentication. Similar to OAuth 1.0a, the user Access Tokens are used to authenticate requests that provide private user account information or perform actions on behalf of another account but, with fine-grained scope for greater control over what access the client application has on the user. 
    
* **[App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens):** You will use this token when making requests to endpoints that responds with information publicly available on Twitter.
    

Since these keys and tokens do not expire unless regenerated, we suggest that you save them in a secure location, such as a password manager, once you've received your credentials.

**Please note: Your keys and tokens will only display once in the [developer portal](https://developer.twitter.com/en/docs/developer-portal), so it is important that you store these credentials in your password management system as soon as you generate them.**

If you misplace or forget the keys and tokens, you will need to regenerate them, which creates new credentials and invalidates the old ones. This means that you will have to update any integrations that you may have set up with your prior credentials.

Learn more about our [authentication best practices](https://developer.twitter.com/en/docs/authentication/guides/authentication-best-practices).