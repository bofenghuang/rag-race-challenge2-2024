platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/api-reference/post-insights-engagement


## Authentication  [¶](#authentication- "Permalink to this headline")

The Engagement API requires the use of HTTPS and supports the use of both User Context and Application-Only OAuth. Most requests to the Engagement API require the use of 3-Legged OAuth (A specific version of User Context), meaning that you use the consumer key and secret of the app that has been registered and approved for Engagement API access by your Twitter account manager, as well as the Tweet owners' access token and access token secret to call the endpoint. The following requests require this type of OAuth:

* Any request to /totals to obtain Impressions and Engagements metric types, which are limited to owned Tweets
* Any request to /28hr
* Any request to /historical

Some requests to the Engagement API can be performed using Application-Only OAuth, meaning that you just need to provide your consumer key and secret, or a bearer token. The following request can be performed with this type of OAuth:

* Any request to /totals to obtain Favorites, Replies, Retweets, or Video Views metric types, which can be retrieved for any Tweet

For any request, you will need to set up a Twitter app and corresponding API key using the app management console available at [developer.twitter.com](https://developer.twitter.com/en/docs/basics/developer-portal/guides/apps).

Please note - You can view and edit your existing [Twitter apps](https://developer.twitter.com/en/docs/basics/developer-portal/guides/apps) via the [Twitter app dashboard](https://developer.twitter.com/en/apps) if you are logged into your Twitter account on developer.twitter.com.

Once you have set up your app, the app ID will need to be approved by your account representative in order for your app to make requests to the Engagement API. Access tokens must be used to represent the “current user”, and requests made on behalf of a separate user must be signed with a valid token. Ensure that you’re [encoding reserved characters](https://tools.ietf.org/html/rfc3986) appropriately within URLs and POST bodies before preparing OAuth signature base strings.

For more information on how to get started with OAuth, please visit the following links:

* [OAuth Overview](https://developer.twitter.com/en/docs/basics/authentication/overview/oauth.html)
* [Using 3 Legged OAuth, also known as User Context](https://developer.twitter.com/en/docs/basics/authentication/overview/3-legged-oauth)
* [Using Application-Only OAuth](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only)