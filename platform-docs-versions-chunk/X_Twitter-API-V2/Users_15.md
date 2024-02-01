platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/lookup/integrate


### Key concepts

#### Authentication

All Twitter API v2 endpoints require requests to be [authenticated](https://developer-staging.twitter.com/en/docs/authentication) with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, App only, or OAuth 2.0 Authorization Code with PKCE to authenticate requests to these endpoints. 

[OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a) requires you to utilize your API Keys, user Access Tokens, and a handful of other parameters to [create an authorization header](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a/authorizing-a-request), which you will then pass with your request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). 

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use OAuth 2.0 to authenticate your requests. If you would like to request a Tweet or private metrics from these endpoints, you will need to use a either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, which will ensure that you have the proper permissions from the user that owns that content.  
 

[App only](https://developer-staging.twitter.com/en/docs/authentication/oauth-2-0) just requires that you pass an [App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) with your request. You can either generate an App only Access Token from directly within a developer App, or generate one using the [POST oauth2/token](https://developer-staging.twitter.com/en/docs/authentication/api-reference/token) endpoint.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

**Please note**

If you are requesting the following fields, OAuth 1.0a User Context or OAuth 2.0 Authorization Code is required: 

* tweet.fields.non\_public\_metrics
* tweet.fields.promoted\_metrics
* tweet.fields.organic\_metrics

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.   
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user. 

The user lookup endpoints are rate limited at both the app-level and the user-level. However, the authenticated user lookup endpoint is rate limited at the user-level

The app-level rate limit means that you, the developer, can only make a certain number of requests to this endpoint over a given period of time from any given App (assumed by the keys and tokens that you are using. The user-level rate limit means that the authenticated user that you are making the request on behalf of can only perform a certain number of times across any developer App.  

The chart below shows the rate limits for each endpoint.

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **HTTP method** | **Rate limit / Level** |
| /2/users | GET | 900 requests per 15 minutes / App and User |
| /2/users/:id | GET | 900 requests per 15 minutes / App and User |
| /2/users/by | GET | 900 requests per 15 minutes / App and User |
| /2/users/by/username/:username | GET | 900 requests per 15 minutes / App and User |
| /2/users/me | GET | 75 requests per 15 minutes / User |

#### Fields and expansions

The Twitter API v2 allows users to select exactly which data they want to return from the API using a set of tools called fields and expansions. The expansion parameter allows you to expand objects referenced in the payload. For example, this endpoint allows you to use the pinned\_tweet\_id expansion.

The fields parameter allows you to select exactly which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) within the different data objects you would like to receive. These endpoints delivers user objects primarily. By default, the user object returns the id, name, and username fields. To receive additional fields such as user.created\_at or user.location, you will have to specifically request those using a fields parameter. Some important fields that you may want to consider using in your integration are our Tweet poll data, metrics, annotations, and conversation ID fields.

We’ve added a guide on how to [use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) in our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).  
  

#### Edge cases

* Tweet text is truncated for Retweets. The short term workaround is to expand the referenced Tweet and retrieve the full text from the expansion. This is a bug that we will fix in the future.