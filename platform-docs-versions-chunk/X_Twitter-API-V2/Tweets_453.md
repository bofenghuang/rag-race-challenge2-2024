platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/integrate


### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. 

These specific endpoints require the use of [OAuth 2.0 Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), which means that you must use a set of keys and user Access Tokens to make a successful request. The Access Tokens must be associated with the user that you are requesting on behalf of. If you want to generate a set of Access Tokens for another user, they must authorize or authenticate your App using an [Authorize URL](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token).

Please note that OAuth 2.0 can be tricky to use. If you are not familiar with this authentication method, we recommend using a [library](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tools-and-libraries) or a tool like Postman to properly authenticate your requests.

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must have a [developer account](https://developer.twitter.com/en/docs/developer-portal), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App. 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user. 

These endpoints are rate limited at the user level, meaning that the authenticated user that you are making the request on behalf of can only call the endpoint a certain number of times across any developer App. There is a user rate limit of 180 requests per 15 min window for the GET method. With the GET method of the Bookmarks lookup endpoint you will get back 800 of your most recent Bookmarked Tweets. Additionally, there is a user rate limit of 50 requests per 15 minutes for the POST and DELETE methods.