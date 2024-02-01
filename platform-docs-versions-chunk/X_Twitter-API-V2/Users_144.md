platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/migrate


### Manage mutes

The v2 manage mutes endpoints will replace the standard v1.1 [POST mutes/users/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-create) and [POST mutes/users/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy) endpoints.

The following tables compare the standard v1.1 and Twitter API v2 mute endpoints:

#### Mute a user

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/mutes/users/create.json | /2/users/:id/muting |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 50 requests per 15 min | 50 requests per 15 min |
| Requires use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |

#### Unmute a user

The following tables compare the standard v1.1 and Twitter API v2 unmute endpoints:

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/mutes/users/destroy.json | /2/users/:source\_user\_id/muting/:target\_user\_id |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 50 requests per 15 min | 50 requests per 15 min |
| Requires use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |