platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/migrate


### Follows lookup

The v2 follows lookup endpoints will replace the standard v1.1 [followers/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids), v1.1 [followers/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-list), v1.1 [friends/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids), and v1.1 [friends/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-list) endpoints.

The following tables compare the various types of follows lookup endpoints:

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | /1.1/friends/ids.json<br><br>/1.1/friends/list.json<br><br>/1.1/followers/ids.json<br><br>/1.1/followers/list.json | /2/users/:id/following<br><br>/2/users/:id/followers |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/en/docs/rate-limits) | 15 requests per 15 min (per user)<br><br>15 requests per 15 min (per app) | 15 requests per 15 min (per user)<br><br>15 requests per 15 min (per app) |
| Maximum users per response | GET friends/id & GET followers/id return a maximum of 5000 users IDs per page.<br><br>  <br><br>GET friends/list & GET followers/list return a maximum of 200 user objects per page. | 1000 user objects per page |
| Pagination | Token returns in a next\_cursor field, which can then be passed as the value to the cursor parameter to return the next page of results. | Token returns in a next\_token field, which can then be passed as the value to the token parameter to return the next page of results.<br><br>The v2 payload also delivers a previous\_token field, which can also be passed with the pagination\_token parameter to return the previous page of results. |
| JSON format | Standard v1.1 format | [Twitter API v2 format](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary) (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Supports selecting which [fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary) return in the payload |     | ✔   |
| Supports the Tweet [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) fields |     | ✔   |
| Supports requesting new [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) fields |     | ✔   |
| Supports the [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field |     | ✔   |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [project](https://developer.twitter.com/en/docs/projects) |     | ✔   |