platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by


### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 900 requests per 15-minute window per each authenticated user |