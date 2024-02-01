platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-show-id


# GET statuses/show/:id

Returns a single [Tweet](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object), specified by the id parameter. The Tweet's author will also be embedded within the Tweet.

See [GET statuses / lookup](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-lookup) for getting Tweets in bulk (up to 100 per call). See also [Embedded Timelines](https://developer.twitter.com/web/embedded-timelines), [Embedded Tweets](https://developer.twitter.com/web/embedded-tweets), and [GET statuses/oembed](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-oembed) for tools to render Tweets according to [Display Requirements](https://about.twitter.com/company/display-requirements).

**About Geo**

If there is no geotag for a status, then there will be an empty `<geo></geo>` or `"geo" : {}`. This can only be populated if the user has used the Geotagging API to send a statuses/update.

The JSON response mostly uses conventions laid out in GeoJSON. The coordinates that Twitter renders are _reversed_ from the GeoJSON specification (GeoJSON specifies a longitude then a latitude, whereas Twitter represents it as a latitude then a longitude), eg: `"geo": { "type":"Point", "coordinates":[37.78029, -122.39697] }`