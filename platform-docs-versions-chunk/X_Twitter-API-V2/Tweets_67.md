platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction

### Reverse chronological home timeline

This endpoint enables you to retrieve the most recent Tweets, Retweets, and replies posted by the authenticated user and the accounts they follow. 

Since you are making requests on behalf of a user, you must authenticate these endpoints using an [OAuth 2.0 Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a). This endpoint has a per-user rate limit of 180 requests per 15-minute window. This endpoint can return every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date.