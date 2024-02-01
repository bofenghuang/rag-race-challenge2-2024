platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/lookup/quick-start/user-lookup


### Steps to build a users lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the GET /users/by endpoint.  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so, this endpoint requires you to authenticate your request with either [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), or [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) authentication methods.

For simplicity's sake, we will utilize App only with this request, but you will need to use one of the other authentication methods if you'd like to request private [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) or users. 

To utilize App only, you must add your keys and tokens, specifically the [App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) (also known as the App only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Identify and specify which user(s) you would like to retrieve

You must specify a user or a set of users that you would like to receive within the request. Depending on which user endpoint you use, you can pass either a user ID or a username. In this situation, we are going to use the [GET /users/by endpoint](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by) which allows you to pass multiple usernames in a single request (rather than the [single-ID](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id), [multi-ID](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users), and [single-username](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username) endpoints) and pass a set of usernames using the usernames query parameter.

Usernames are simply the account handle that you can find within an account's profile URL. For example, the following account’s username is twitterdev.

`https://twitter.com/TwitterDev`

In Postman, navigate to the "Params" tab and enter this username, or a string of usernames separated by a comma, into the "Value" column of the username parameter, making sure to not include any spaces between usernames and commas. 

|     |     |
| --- | --- |
| **Key** | **Value** |
| `username` | twitterdev,twitterapi,adsapi |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) fields in your response: id, name, and username.

If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the [field](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [expansion](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request a three additional sets of fields from different objects:

1. The additional user.created\_at field in the primary user objects.
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
3. The additional  tweet.created\_at field in the associated Tweet objects.  
     

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| `user.fields` | `created_at` | `user.created_at` |
| `expansions` | `author_id` | tweet.id, tweet.text |
| `tweet.fields` | `created_at` | `includes.users.created_at` |

You should now see the following URL next to the "Send" button:

      `https://api.twitter.com/2/users/by?usernames=twitterdev,twitterapi,adsapi&user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at`
    

####   
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

      `{   "data": [     {       "created_at": "2013-12-14T04:35:55.000Z",       "id": "2244994945",       "name": "Twitter Dev",       "pinned_tweet_id": "1255542774432063488",       "username": "TwitterDev"     },     {       "created_at": "2007-05-23T06:01:13.000Z",       "id": "6253282",       "name": "Twitter API",       "username": "TwitterAPI"     },     {       "created_at": "2013-02-27T20:01:12.000Z",       "id": "1225933934",       "name": "Twitter Ads API",       "username": "AdsAPI"     }   ],   "includes": {     "tweets": [       {         "author_id": "2244994945",         "created_at": "2020-04-29T17:01:38.000Z",         "id": "1255542774432063488",         "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. \n\nWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId"       }     ]   } }`