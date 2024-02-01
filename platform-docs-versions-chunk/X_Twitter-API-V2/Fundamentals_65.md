platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/metrics


### Terminology

* **Authorized account**: Twitter account that has authorized your [Twitter developer app](https://developer.twitter.com/en/docs/apps/overview) by granting it access to that account (any [app permission level](https://developer.twitter.com/en/docs/apps/app-permissions) will permit access to Tweet metrics). This can be achieved using the [Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) or [3-legged OAuth](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) process.
* **Owned account**: Twitter account linked to your [Twitter developer app](https://developer.twitter.com/en/docs/apps/overview).
* **Public metrics**: Metrics’ totals that are available for anyone to access on [Twitter](https://twitter.com/home), such as number of likes and number of Retweets.
* **Non-public metrics**: Metrics’ totals that are not available for anyone to view on [Twitter](https://twitter.com/home), such as number of impressions and video view quartiles. Requires [OAuth 2.0](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) user context authentication.
* **Organic metrics**: Grouping of public and non-public metrics attributed to an organic context (posted and viewed in a regular manner). Requires [OAuth 2.0](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) user context authentication.
* **Promoted metrics**: Grouping of public and non-public metrics attributed to a promoted context (posted or viewed as part of an Ads campaign). Requires [OAuth 2.0](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) user context authentication and that the Tweet was promoted in an Ad. Promoted metrics are not included in these counts when a Twitter user is using their own Ads account to promote another Twitter user's Tweets. Promoted metrics are included in these counts when:
    * a Twitter user promotes their own Tweets
    * in an Ads account for a specific handle, the admin for that account may add another Twitter user as an account user so this second account user can promote Tweets for the handle