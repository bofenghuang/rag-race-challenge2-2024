platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/migrate


## Comparing Twitter API’s List lookup endpoints

The v2 List lookup endpoint group will replace the standard v1.1 [GET lists/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-show) and  [GET lists/ownership](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-ownerships) endpoints. If you have code, apps, or tools that use one of these versions of the List lookup endpoints, and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you.

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:

**List Lookup by ID**

|     |     |     |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/show.json` | `/2/lists/:id` |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 75 requests per 15 min with OAuth 1.0a<br><br>75 requests per 15min with OAuth 2.0<br><br>75 requests per 15 min with App only | 75 requests per 15 min with OAuth 1.0a<br><br>75 requests per 15 min with OAuth 2.0<br><br>75 requests per 15 min with App only |

**User owned List lookup**

|     |     |     |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/ownerships.json` | `/2/users/:id/owned_lists` |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 15 requests per 15 min with OAuth 1.0a<br><br>15 requests per 15 min with App only | 15 requests per 15 min with OAuth 1.0a<br><br>15 requests per 15min with OAuth 2.0<br><br>15 requests per 15 min with App only |

To access the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info). When authenticating, you must use keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) page.

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)