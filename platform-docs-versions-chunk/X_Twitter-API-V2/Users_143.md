platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/migrate


### Mutes lookup

The v2 mutes lookup endpoint will replace the standard [v1.1 GET mutes/users/ids](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-ids) and [GET mutes/users/list](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-list) endpoints.

The following tables compare the standard v1.1 and Twitter API v2 mute endpoints:  
 

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | ******GET****** | ******GET****** |
| Host domain | ******https://api.twitter.com****** | ******https://api.twitter.com****** |
| Endpoint path | ******/1.1/mutes/users/ids.json******<br><br>/1.1/mutes/users/list.json | ******/2/users/:id/muting****** |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 15 requests per 15 min (per user) | 15 requests per 15 min (per user) |
| Data formats | Standard v1.1 format | [Twitter API v2 format](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary) (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Requires use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |