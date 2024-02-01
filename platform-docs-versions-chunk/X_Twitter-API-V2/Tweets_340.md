platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/migrate/retweets-lookup-standard-to-twitter-api-v2

### Similarities

#### **Authentication**

Both the standard v1.1 and Twitter API v2 Retweets lookup endpoints ([v1.1 GET statuses/retweets/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets-id) and [v1.1 GET statuses/retweeters/:ids](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids)) use [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a) or OAuth 2.0 Bearer Token.

**Users per request limits**

For both v1.1 and v2 GET endpoints the max number of users that will be returned by the Retweets lookup endpoint is 100 users per page. For the v2 Retweets lookup endpoint, you can use pagination tokens to page through large results.