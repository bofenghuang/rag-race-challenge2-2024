platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/introduction

### Follows lookup

The follows lookup endpoints enable you to explore and analyze relationships between users, which is sometimes called network analysis. Specifically, there are two REST endpoints that return [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) representing who a specified user is following, or who is following a specified user.

You can authenticate this endpoint with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). You can request up to 1,000 users per request, and pagination tokens will be provided for paging through large sets of results.