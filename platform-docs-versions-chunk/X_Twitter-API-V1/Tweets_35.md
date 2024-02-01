platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-oembed

GET statuses/oembed

get-statuses-oembed

# GET statuses/oembed

Returns a single Tweet, specified by either a Tweet web URL or the Tweet ID, in an [oEmbed](http://oembed.com/)\-compatible format. The returned HTML snippet will be automatically recognized as an [Embedded Tweet](https://developer.twitter.com/web/embedded-tweets) when [Twitter's widget JavaScript is included on the page](https://developer.twitter.com/web/javascript/loading).

The oEmbed endpoint allows customization of the final appearance of an Embedded Tweet by setting the corresponding properties in HTML markup to be interpreted by Twitter's JavaScript bundled with the HTML response by default. The format of the returned markup may change over time as Twitter adds new features or adjusts its Tweet representation.

The Tweet fallback markup is meant to be cached on your servers for up to the suggested cache lifetime specified in the `cache_age`.