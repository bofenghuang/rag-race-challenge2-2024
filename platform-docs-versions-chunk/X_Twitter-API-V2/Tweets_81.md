platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/integrate


### Key concepts

#### Authentication

All Twitter API v2 endpoints require requests to be [authenticated](https://developer.twitter.com/en/docs/authentication) with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE to authenticate requests to these endpoints. You can use OAuth 2.0 App-Only for user Tweets timeline and user mentions timeline.

[OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a) requires you to utilize your API Keys, user Access Tokens, and a handful of other parameters to [create an authorization header](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a/authorizing-a-request), which you will then pass with your request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). 

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use OAuth 2.0 to authenticate your requests. If you would like to request a Tweet or private metrics from these endpoints, you will need to use a either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, which will ensure that you have the proper permissions from the user that owns that content.

[OAuth 2.0 App-Only](https://developer-staging.twitter.com/en/docs/authentication/oauth-2-0) just requires that you pass an [OAuth 2.0 App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) with your request. You can either generate an App Access Token from directly within a developer App, or generate one using the [POST oauth2/token](https://developer-staging.twitter.com/en/docs/authentication/api-reference/token) endpoint. You can use this for user Tweets timeline or user mention timeline.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

**Please note**

If you are requesting the following [fields](https://developer.twitter.com/en/docs/twitter-api/fields), OAuth 1.0a User Context or OAuth 2.0 Authorization Code is required: 

* `tweet.fields.non_public_metrics`
* `tweet.fields.promoted_metrics`
* `tweet.fields.organic_metrics`
* `media.fields.non_public_metrics`
* `media.fields.promoted_metrics`
* `media.fields.organic_metrics`

#### [](https://developer.twitter.com/en/docs/twitter-api/pagination)Developer portal, Projects, and developer Apps

To work with any Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. Your keys and tokens within that developer App will work for these timelines endpoints.  
  

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the volume, [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests that every developer can make on behalf of an app or on behalf of an authenticated user. 

There are different rate limits applied for these endpoints depending on which authentication method is being used. The app-level rate limits apply to an App making requests using OAuth 2.0 App-Only, whereas the user-level rate limit applies to requests being made on behalf of the specific authorizing user using OAuth 1.0a User Context. These two rate limits are based on the frequency of requests within a 15-minute window.  

For example, an app using OAuth 2.0 App-Only auth for both of these timelines endpoints, can make 1500 requests (including pagination requests) to the user Tweet timeline, and 450 requests (including pagination requests) to the user mention timeline within a 15-minute timeframe.  That same app, within the same 15-minute timeframe, with two different authorized users (using OAuth 1.0a User Context) can make 900 requests (including pagination requests) to the user Tweet timeline, and 180 requests (including pagination requests) to the user mention timeline for each authenticated user. 

Reverse chronological home timeline has a per-user rate limit of 180 requests per a 15 min window. With this endpoint you can return every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date.

#### Fields and expansions  

The Twitter API v2 allows you to select exactly which data you want returned from the API using [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions). The expansion parameter allows you to expand objects referenced in the payload. For example, this endpoint allows you to request poll, place, media, and other objects using the expansions parameter.

The fields parameter allows you to select exactly which fields within the different data objects you would like to receive. By default, the primary Tweet object returned by these endpoints include the id and text fields. To receive additional fields such as author\_id or public\_metrics, you will have to specifically request those using the fields parameters. Some important fields that you may want to consider using in your integration are our poll data, [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics), [Tweet annotations](https://developer.twitter.com/en/docs/twitter-api/annotations), and [conversation ID](https://developer.twitter.com/en/docs/twitter-api/conversation-id) fields.

We’ve added a guide on [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) together to our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary).  
  

#### Tweet metrics

The Twitter API v2 endpoints allow you to request Tweet metrics directly from the returned Tweet object, assuming you pass the proper fields with your request.

There are some limitations with Tweet metrics that you should be aware of, specifically related to user privacy and the following response fields:

* `tweet.fields.non_public_metrics`
* `tweet.fields.promoted_metrics`
* `tweet.fields.organic_metrics`
* `media.fields.non_public_metrics`
* `media.fields.promoted_metrics`
* `media.fields.organic_metrics`

  
The noted fields include private metrics data, meaning you must be authorized by the Tweet’s publisher to retrieve this data on their behalf when using the user Tweet timeline endpoint, meaning you must use [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

For example, in order to receive non\_public\_metrics for user ID 1234's user Tweet timeline you will need to include access tokens associated with that user in your request. You can have users authorize your app and receive a set of access tokens associated with them by using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). 

If you are using user mention timeline, the noted fields will not be available unless the mentioning author has authorized your App to access their private metrics data and you are using that user’s access tokens when making the request with OAuth 1.0a User Context.

All non\_public\_metrics, organic\_metrics, and promoted\_metrics are only available for Tweets created in the last 30 days. This means that when you are requesting the noted fields, the results will automatically adjust to only include Tweets from the last 30 days.

If these noted fields are requested, only Tweets that are authored by the authenticated user will be returned, all other Tweets will receive an error message.  
  

#### Pagination

These endpoints utilize pagination so that responses are returned quickly. In cases where there are more results than what can be sent in a single response (up to 100 Tweets for the timelines endpoints) you will need to paginate. Use the max\_results parameter to identify how many results will return per page, and the pagination\_token parameter return the next page of results. You can learn more by reviewing our [pagination guide](https://developer.twitter.com/en/docs/twitter-api/pagination).  
  

#### Filtering results

These endpoints include several parameters that you can use to filter results. Using start\_date and end\_date, you can narrow down results to a specific timeframe. If you’d rather use Tweet IDs to select a specific set of Tweets, you can use the since\_id and until\_id. The user Tweets timeline also has an exclude parameter that can remove Retweets and Replies from your results.   
  

#### Tweet caps and volume of Tweets returned

The user Tweet timeline and user mention timeline endpoints are limited in the number of Tweets that they can return in a given month. The reverse chronological home timeline endpoint is not subject to this limitation.

Regardless of which timelines endpoint you use, the Tweets returned will count towards the Project-level [Tweet caps](https://developer.twitter.com/en/docs/twitter-api/tweet-caps). Usage is shown in the developer portal, and the 'month' starts on your subscription renewal day shown on the [developer portal dashboard](https://developer.twitter.com/en/portal/dashboard). 

The user Tweet timeline endpoint will only return the most recent 3200 Tweets posted to a user’s timeline. Setting start\_time and end\_time to a time period that includes Tweets beyond the 3200 most recent, you will receive a successful response, but no Tweets.

It is also important to note that, if you pass the excludes=replies with your user Tweet timeline requests, only the most recent 800 Tweets will be returned.

The user mention timeline endpoint will only return the most recent 800 Tweet mentions.

The reverse chronological home timeline endpoint returns the last 3200 Tweets.  
  

#### Tweet edits

Tweets that are eligible for edits can be edited up to five times in the 30 minutes after the original Tweet was published. The search endpoints will always provide the latest version of the Tweet. If you only request Tweets that were published 30 or more minutes ago, you will always receive the final version of the Tweet. However, if you have a near-real-time use case, and are querying Tweets published within the last thirty minutes, those Tweets could have been edited after you received them. These Tweets can be rehydrated with search, or the Tweet Lookup endpoint to confirm their final state. To learn more about how Tweet edits work, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/edit-tweets) page.    

#### Edge cases

* When requesting non-public metrics on the User Tweet timeline endpoint for Tweets that are older than 30 days, you may see a next\_token in the response with a result count of 0. To avoid encountering this issue, ensure that the timeframe requested with the non\_public\_metrics parameter is within the most recent 30 days. Additionally, the max\_results minimum value should be 10. These may help to avoid this scenario, but this could still occur.
* Requesting promoted metrics for Tweets that were not promoted returns an empty response, instead of Tweet data. Our team is currently working on fixing this issue.

* For a Retweet that contains Tweet body text greater than 140 characters in length, the text field will be truncated instead of returning the full Tweet text. The short term workaround is to expand the referenced Tweet and retrieve the full text from the expansion. This is a bug that we will fix in the future.