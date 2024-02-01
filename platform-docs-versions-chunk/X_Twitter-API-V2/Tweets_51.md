platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/migrate/manage-tweets-standard-to-twitter-api-v2

### Similarities

#### **Authentication**

Both the standard v1.1 and Twitter API v2 manage Tweets ([POST statuses/update](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update) and [POST statuses/destroy/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-destroy-id)) endpoints use [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a). Therefore, if you were previously using one of the standard v1.1 endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.