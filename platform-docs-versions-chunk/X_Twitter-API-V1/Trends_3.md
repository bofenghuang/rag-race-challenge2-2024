platform: X
topic: Twitter-API-V1
subtopic: Trends
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Trends.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/trends/trends-for-location/api-reference/get-trends-place


# GET trends/place

Returns the top 50 trending topics for a specific `id`, if trending information is available for it.

Note: The `id` parameter for this endpoint is the "where on earth identifier" or WOEID, which is a legacy identifier created by Yahoo and has been deprecated. Twitter API v1.1 still uses the numeric value to identify town and country trend locations. Reference our legacy [blog post](https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html), or [archived data](https://archive.org/details/geoplanet_data_7.10.0.zip0.)

Example WOEID locations include: Worldwide: 1 UK: 23424975 Brazil: 23424768 Germany: 23424829 Mexico: 23424900 Canada: 23424775 United States: 23424977 New York: 2459115

To identify other ids, please use the [GET trends/available](https://developer.twitter.com/en/docs/twitter-api/v1/trends/locations-with-trending-topics/api-reference/get-trends-available) endpoint.

The response is an array of `trend` objects that encode the name of the trending topic, the query parameter that can be used to search for the topic on [Twitter Search](http://search.twitter.com/), and the Twitter Search URL.

The most up to date info available is returned on request. The `created_at` field will show when the oldest trend started trending. The `as_of` field contains the timestamp when the list of trends was created.

The `tweet_volume` for the last 24 hours is also returned for many trends if this is available.