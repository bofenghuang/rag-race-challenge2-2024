platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/lookup/migrate


## Comparing Twitter API’s users lookup endpoints

The v2 user lookup endpoints will replace the standard v1.1 [GET users/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup.html) and [GET users/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-show.html) endpoints. If you have code, apps, or tools that use one of these versions of the user lookup endpoints, and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you.   
 

The following tables compare the various types of users lookup endpoints:  
 

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/users/show.json` `/1.1/users/lookup.json` | `/2/users`<br><br>`/2/users/:id`<br><br>`/2/users/by`<br><br>`/2/users/by/:username` |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>App only<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/en/docs/rate-limits) | 900 requests per 15 min (per user)<br><br>/show - 900 requests per 15 min (per app)  <br>/lookup - 300 requests per 15 min (per app) | 900 requests per 15 min (per user)<br><br>300 requests per 15 min (per app) |
| Maximum Users per response | /show -  1<br><br>/lookup - 100 | 100 |
| JSON response object format | Standard v1.1 format | [Twitter API v2 format](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary) (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Supports selecting which [fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary) return in the payload |     | ✔   |
| Supports the [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) fields (on pinned Tweet) |     | ✔   |
| Supports requesting new [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) fields (on pinned Tweet) |     | ✔   |
| Supports the [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field (on pinned Tweet) |     | ✔   |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [project](https://developer.twitter.com/en/docs/projects) |     | ✔   |