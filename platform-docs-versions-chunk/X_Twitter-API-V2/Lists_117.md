platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/migrate/list-members-lookup-standard-to-twitter-api-v2

### Similarities

#### **Authentication**

Both endpoint versions support both [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a) and [App only](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0). Therefore, if you were previously using one of the standard v1.1 List members endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.

Depending on your authentication library/package of choice, App only authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate an App only Access Token, see [this App only guide](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only).