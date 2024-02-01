platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/integrate


### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. 

These specific endpoints requires the use of [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), which means that you must use a set of API keys and user Access Tokens to make a successful request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize or authenticate your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/content/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use OAuth 2.0 to authenticate your requests.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must have a [developer account](https://developer.twitter.com/en/docs/developer-portal), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.   
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user.   

These endpoints are rate limited at the user level, meaning that the authenticated user that you are making the request on behalf of can only call the endpoint a certain number of times across any developer App. There is a user rate limit of 200 requests per 15 minutes for the POST method. The DELETE method has a rate limit of 50 requests for 15 minutes. Additionally, there is a limit of [300 requests per 3 hours](https://blog.twitter.com/developer/en_us/topics/tools/2018/new-developer-requirements-to-protect-our-platform), including Tweets created with either manage Tweets or manage Retweets.  
 

#### Source labels

Your App name and website URL will be shown as the [source label](https://help.twitter.com/en/using-twitter/how-to-tweet#source-labels) within metadata for any Tweets created programmatically by your application. If you change the use case of a Twitter App, be sure to update the use case in these settings in order to ensure you are in compliance with the [Developer Terms](https://developer.twitter.com/content/developer-twitter/en/developer-terms/agreement-and-policy).  
 

#### Profile settings

You can only add a location to Tweets if you have geo enabled in your profile settings. If you don’t have geo enabled, you can still add a location parameter in your request body, but it won’t get attached to your Tweet. The same is also true for tagging users in images. If the user you’re tagging doesn’t have photo-tagging enabled, their names won’t show up in the list of tagged users even though the Tweet is successfully created.  

#### Adding media to a Tweet

#### Currently, isn’t a way to fully upload media using v2 of the Twitter API currently. However, you attach previously uploaded media to a Tweet. You can use media IDs that have been already [uploaded using the v1 media endpoint](https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload) or [Twitter Media Studio](https://media.twitter.com/en/articles/products/2018/media-studio). These media ids must be your own or that of an authenticated user.