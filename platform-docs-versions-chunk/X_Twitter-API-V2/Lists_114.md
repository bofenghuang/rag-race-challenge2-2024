platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/migrate


### Manage List members

The v2 manage List members endpoints will replace the standard [POST lists/members/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create), [POST lists/members/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy) endpoints.

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:

**Add member**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/members/create.json | /2/lists/:id/members |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | None | 300 requests per 15 min (per user) |

**Remove member**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/members/destroy.json | /2/lists/:id/:user\_id |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | None | 300 requests per 15 min (per user) |

To access the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info). When authenticating, you must use keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) page.

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)