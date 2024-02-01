platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/integrate


### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, App only, or OAuth 2.0 Authorization Code with PKCE to authenticate your requests to this endpoint. 

[OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), which means that you must use a set of API Keys and user Access Tokens to make a successful request. The access tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/content/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use either OAuth 2.0 or App only to authenticate your requests.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

[App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0) just requires that you pass an [App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) with your request. You can either generate an App only Access Token directly within a developer App, or generate one using the [POST oauth2/token](https://developer.twitter.com/en/docs/authentication/api-reference/token) endpoint.

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.  
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests you can make on behalf of your app or on behalf of an authenticated user. 

This endpoint is rate limited at both the App-level and the user-level. The app rate limit means that you, the developer, can only make a certain number of requests to this endpoint over a given period of time from any given App (assumed by using either the API Key and API Secret Key, or the Bearer Token). The user rate limit means that the authenticated user that you are making the request on behalf of can only perform a List Tweet lookup a certain number of times across any developer App.

The chart below shows the rate limits for each endpoint.

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **HTTP method** | **Rate limit** |
| /2/lists/:id/tweets | GET | 900 requests per 15 minutes |

Fields and expansions  

The Twitter API v2 GET endpoint allows users to select exactly which data they want to return from the API using a set of tools called `fields` and `expansions`. The `expansions` parameter allows you to expand objects referenced in the payload. For example, looking up List Tweets allows you to pull the following [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions):

* `author_id`
    

The `fields` parameter allows you to select exactly which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) within the different data objects you would like to receive. This endpoint delivers Tweet objects primarily. By default, the Tweet object returns the `id`, and `text` fields. To receive additional fields such as `tweet.created_at` or `tweet.lang`, you will have to specifically request those using a fields parameter. 

We’ve added a guide on using [fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) together to our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

 The chart below shows the field and expansions available for the lookup endpoint:

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **Fields** | **Expansions** |
| /2/lists/:id/tweets | `tweet.fields`<br><br>`user.fields` | `author_id` |

Pagination  

Looking up List Tweets can return a lot of data. To ensure we are returning consistent, high-performing results at any given time, we use pagination. Pagination is a feature in Twitter API v2 endpoints that return more results than can be returned in a single response. When that happens, the data is returned in a series of 'pages'. Learn more about how to [paginate through results.](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/pagination)