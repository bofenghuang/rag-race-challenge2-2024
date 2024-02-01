platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/migrate/manage-retweets-standard-to-twitter-api-v2

### Similarities

#### Authentication

Both the standard v1.1 and Twitter API v2 manage Retweets ([POST statuses/retweet/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-retweet-id), and [POST statuses/unretweet/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id)) endpoints use [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a). Therefore, if you were previously using one of the standard v1.1 Retweets lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.