platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/introduction


## Introduction

Direct Messages enable private conversations on Twitter. Direct Messages are one of the most popular features of Twitter, with a wide variety of use cases. These use cases range from group chats among friends to powering customer support for brands around the world. New v2 versions of Direct Messages endpoints will be introduced in stages, and this first stage includes fundamental endpoints for creating Direct Messages and listing Direct Message conversation events. For the first time, the Twitter API v2 supports _group_ conversations.

This initial release of Direct Messages lookup includes three GET methods:

* **GET /2/dm\_conversations/with/:participant\_id/dm\_events** \- Retrieves Direct Message events associated with a one-to-one conversation. The :participant\_id path parameter is the User ID of the account having the conversation with the authenticated user making this request. 
* **GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events** - Retrieves Direct Message events associated with a specific conversation ID, as indicated by the :dm\_conversation\_id path parameter. 
* **GET /2/dm\_events** - Retrieves Direct Message events associated with a user, including both one-to-one and group conversations. Events from up to 30 days ago are available.  

Note that Direct Message event IDs are common across the v1.1 and v2 (as well as the Twitter App), so the v1.1 method to list a single event can be used along with these new v2 endpoints. Also note that the Enterprise and Premium Account Activity APIs support v2 one-to-one messages, but do not yet support group conversations.   

With this release, three event types are supported, and these endpoints support query parameters to filter on them:

* **MessageCreate** - A message has been created. 
* **ParticipantsJoin** - A new participant has joined a conversation. 
* **ParticipantsLeave** - A participant has left a conversation. 

There is a user rate limit of 300 requests per 15 minutes for the GET methods. This rate limit is shared across these GET endpoints.

Since you are making requests on behalf of a user with Direct Message v2 endpoints, you must authenticate with either [OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), using Access Tokens associated with users that have authorized your Twitter App. To generate these Access Tokens with OAuth 1.0a, you can use the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens). To generate user Access Tokens with OAuth 2.0, you can use the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token).

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/tweets&method=get)