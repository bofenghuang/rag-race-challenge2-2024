platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/migrate


### List members lookup

The v2 List members lookup endpoints will replace the standard  [GET lists/members](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members), [GET lists/memberships](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships), endpoints.

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:

**List member Lookup**

|     |     |     |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/members.json` | `/2/lists/:id/members` |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 900 requests per 15 min with OAuth 1.0a<br><br>75 requests per 15min with App only | 900 requests per 15 min with OAuth 1.0a<br><br>900 requests per 15 min with OAuth 2.0<br><br>900 requests per 15 min with App only |

**List membership lookup**

|     |     |     |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/memberships.json` | `/2/users/:id/list_memberships` |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 75 requests per 15 min with OAuth 1.0a<br><br>75 requests per 15min with App only | 75 requests per 15 min with OAuth 1.0a<br><br>75 requests per 15 min with OAuth 2.0<br><br>75 requests per 15min with App only |