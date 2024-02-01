platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/migrate


## Comparing Twitter API’s Tweets lookup endpoints

The v2 Tweets lookup endpoints will replace the standard v1.1 [GET statuses/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-lookup) and [GET statuses/show](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-show-id) endpoints, as well as the Labs [Tweet lookup](https://developer.twitter.com/en/docs/labs/tweets-and-users) endpoints. If you have code, apps, or tools that use one of these versions of the Tweet lookup endpoint, and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you. 

The following tables compare the various types of Tweets lookup endpoints:  
 

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/statuses/show.json` `/1.1/statuses/lookup.json` | `/2/tweets` |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 App-Only<br><br>OAuth 2.0 Authorization Code with PKCE |
| Tweet [JSON format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction) | Standard v1.1 format | [Twitter API v2 format](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary) (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Supports selecting which [fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary) return in the payload |     | ✔   |
| Supports the [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) fields |     | ✔   |
| Supports requesting new [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) fields |     | ✔   |
| Supports the [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field |     | ✔   |
| Provides Tweet edit history | ✔   | ✔   |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |