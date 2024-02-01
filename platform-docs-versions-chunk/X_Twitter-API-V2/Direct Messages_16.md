platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/integrate

### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must have an approved developer account, set up a Project within that account, and create a developer App within that Project. You can then find your keys and tokens within your developer App. 

### Rate limits

Everyday many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, rate limits are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user. 

The Direct Message lookup endpoints are rate limited at the user-level, meaning that the authenticated user that you are making the request on behalf of can only make a certain number of requests with your Twitter App. There is a user rate limit of 300 requests per 15 minutes for the GET methods. These rate limits are shared across the GET endpoints.