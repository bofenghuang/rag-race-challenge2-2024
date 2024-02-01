platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/lookup/quick-start/authenticated-lookup


### Steps to build an authenticated user lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Authenticated User Lookup” folder, and select “Lookup an Authenticated User”.

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

Step three: Determine which user fields you want to retrieve  

If you click the "Send" button after step three, you will receive the default [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) fields in your response: id, name, and username.

If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the [field](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [expansion](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request three additional sets of fields from different objects:

1. The additional user.created\_at field in the primary user objects.
    
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
    
3. The additional tweet.created\_at field in the associated Tweet objects.  
    

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| user.fields | created\_at | user.created\_at |
| expansions | pinned\_tweet\_id | includes.tweets.id,  <br>includes.tweets.text |
| tweet.fields | created\_at, author\_id | includes.tweets.created\_at, includes\_tweets.author\_id |

You should now see a similar URL next to the “Send” button:

      `https://api.twitter.com/2/users/me?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at`