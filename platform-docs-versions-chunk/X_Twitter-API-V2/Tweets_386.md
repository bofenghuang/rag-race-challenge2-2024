platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/introduction

### Likes lookup

With endpoints in the Likes lookup group, you can retrieve a list of accounts that have liked a Tweet, or a list of Tweets that an account has liked. These endpoints include:

* Tweets liked by a user - GET /2/users/:id/liked\_tweets
* Users who have liked a Tweet - GET /2/tweets/:id/liking\_users

You can authenticate these endpoints with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0). For the liked Tweets endpoints, pagination tokens will be provided for paging through large sets of results.

The liking users endpoint limits you to a total of 100 liking accounts per tweet for all time.  Additionally, the liked Tweets endpoint is also subject to the monthly [Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps) applied at the Project level.