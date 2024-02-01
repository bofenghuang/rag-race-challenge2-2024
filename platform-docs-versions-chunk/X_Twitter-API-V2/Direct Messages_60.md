platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/integrate

### Rate limits

Everyday many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, rate limits are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user.   

The Manage Direct Message endpoints are rate limited at both the per-user and Twitter App levels. This means that the authenticated user that you are making the request on behalf of can only send a certain number of messages with your Twitter App. In addition, there is a daily limit on how many Direct Messages can be sent by your Twitter App.   

There is a user rate limit of 200 requests/messages per 15 minutes for the POST methods. Users are also limited to 1000 Direct Messages per 24 hours. In addition, Twitter Apps have a limit of 15000 messages per 24 hours. These rate limits are shared across the POST endpoints.