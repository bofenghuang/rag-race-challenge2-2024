platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/introduction


### Manage follows

The manage follows endpoints enable you to follow or unfollow users.

Since you are making requests on behalf of a user, you must authenticate these endpoints with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and utilize the user Access Tokens associated with the user you are making the request on behalf of. You can generate this user Access Token using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) (OAuth 1.0a) or using the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).

You are limited to 400 follow actions per day on behalf of each authenticated user, and will be limited to 1,000 actions per day per App across all of your authenticated users. For example, if you have five authenticated users, you can follow 400 users per day (per user limit) with two of those users for a total of 800 actions, and will have to split the remaining 200 actions (per app) amongst the remaining three users. This limit does not apply to the unfollow endpoint, which has a separate limit of 500 actions per day (per app).

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/users/follows/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Ffollowers&method=get)