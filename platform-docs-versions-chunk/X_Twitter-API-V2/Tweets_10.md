platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/integrate


### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, OAuth 2.0 App-Only, or OAuth 2.0 Authorization Code with PKCE to authenticate your requests to these endpoints. 

[OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) requires you to utilize your API Keys, user Access Tokens, and a handful of other parameters to [create an authorization header](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/authorizing-a-request), which you will then pass with your request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). 

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use OAuth 2.0 to authenticate your requests. If you would like to request a Tweet or private metrics from these endpoints, you will need to use a either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, which will ensure that you have the proper permissions from the user that owns that content.  
 

[OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0) just requires that you pass an [OAuth 2.0 App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) with your request. You can either generate an App Access Token from directly within a developer App, or generate one using the [POST oauth2/token](https://developer.twitter.com/en/docs/authentication/api-reference/token) endpoint.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

**Please note**

If you are requesting the following fields, OAuth 1.0a User Context or OAuth 2.0 Authorization Code is required: 

* tweet.fields.non\_public\_metrics
* tweet.fields.promoted\_metrics
* tweet.fields.organic\_metrics
* media.fields.non\_public\_metrics
* media.fields.promoted\_metrics
* media.fields.organic\_metrics

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must have an approved [developer account](https://developer.twitter.com/en/docs/developer-portal), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.   
  
Rate limits

Everyday, many thousands of developers make requests to the Twitter API, and in order to manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) are placed on each endpoint. Rate limits number the requests that you can make on behalf of your app or on behalf of an authenticated user. 

This endpoint is rate limited at both the App-level and the user-level. The app rate limit means that you, the developer, can only make a certain number of requests to this endpoint over a given period of time from any given App (assumed by using either the API Key and API Secret Key, or the App Access Token). The user rate limit means that the authenticated user that you are making the request on behalf of can only perform a Tweets lookup a certain number of times across any developer App.  
  
Fields and expansions

The Twitter API v2 allows users to select exactly which data they want to return from the API using a set of tools called fields and expansions. The expansion parameter allows you to expand objects referenced in the payload. For example, this endpoint allows you to pull the following [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions):

* edit\_history\_tweet\_ids
* attachments.poll\_ids
* attachments.media\_keys
* author\_id
* entities.mentions.username
* geo.place\_id
* in\_reply\_to\_user\_id
* referenced\_tweets.id
* referenced\_tweets.id.author\_id  
    

  
The fields parameter allows you to select exactly which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) within the different data objects you would like to receive. These endpoints deliver Tweet objects primarily. By default, the Tweet object returns the id,  text, and edit\_history\_tweet\_ids fields. To receive additional fields such as tweet.created\_at or tweet.entities, you will have to specifically request those using a fields parameter. When you include edit\_controls, you will receive information about whether the Tweet was ever eligible for edits, a timestamp indicating whether the 30-minute edit period has ended, and how many edit opportunities remain. Other important fields that you may want to consider using in your integration are our poll data, metrics, Tweet annotations, and conversation ID fields.

We’ve added a guide on how to [use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) in our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).  
  

#### Tweet edits

Tweets that are eligible for edits can be edited up to five times in the 30 minutes after the original Tweet was published. The Tweet lookup endpoint will always provide the latest version of the Tweet. If you only request Tweets that were published 30 or more minutes ago, you will always receive the final version of the Tweet. However, if you have a near-real-time use case, and are querying Tweets published within the last thirty minutes, those Tweets could have been edited after you received them. To learn more about how Tweet edits work, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/edit-tweets) page.    

#### Edge cases

* Requesting promoted metrics for Tweets that were not promoted returns an empty response, instead of Tweet data. Our team is currently working on fixing this issue.
* Tweet text is truncated for Retweets. The short-term workaround is to expand the referenced Tweet and retrieve the full text from the expansion. This is a bug that we will fix in the future.