platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/metrics


### Private metrics (non-public, organic metrics)

In the following request, we are requesting non-public metrics with more details or organic metrics, meaning which of these metrics were generated in an organic context, on the Tweet and attached video with the following fields and expansion. Since these fields are private (not available to view on Twitter.com),Requires [OAuth 2.0](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) user context authentication. is required for the request. Check out our [guide](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/creating-a-signature) that explains how to generate the OAuth 1.0a signature sampled below.

* `tweet.fields=non_public_metrics,organic_metrics`
* `expansions=attachments.media_keys&media.fields=non_public_metrics,organic_metrics`

**Sample Request**

      `curl 'https://api.twitter.com/2/tweets/1204084171334832128?tweet.fields=non_public_metrics,organic_metrics&media.fields=non_public_metrics,organic_metrics&expansions=attachments.media_keys' --header 'authorization: OAuth oauth_consumer_key="CONSUMER_API_KEY", oauth_nonce="OAUTH_NONCE", oauth_signature="OAUTH_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="OAUTH_TIMESTAMP", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'`
    

**Sample Response**

      `{   "data": {     "attachments": {       "media_keys": [         "13_1204080851740315648"       ]     },     "id": "1263145271946551300",     "non_public_metrics": {       "impression_count": 956,       "url_link_clicks": 9,        "user_profile_clicks": 34     },     "organic_metrics": {       "impression_count": 956,       "like_count": 49,       "reply_count": 2,       "retweet_count": 9,       "url_link_clicks": 9,        "user_profile_clicks": 34     },     "text": "test"   },   "includes": {     "media": [       {         "media_key": "13_1204080851740315648",         "non_public_metrics": {           "playback_0_count": 0,           "playback_100_count": 1,           "playback_25_count": 2,           "playback_50_count": 1,           "playback_75_count": 1         },         "organic_metrics": {           "playback_0_count": 0,           "playback_100_count": 1,           "playback_25_count": 2,           "playback_50_count": 1,           "playback_75_count": 1,           "view_count": 1         },         "type": "video"       }     ]   } }`