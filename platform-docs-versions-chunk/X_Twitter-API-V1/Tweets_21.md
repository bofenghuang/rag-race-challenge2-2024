platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update


# POST statuses/update

Updates the authenticating user's current status, also known as Tweeting.

For each update attempt, the update text is compared with the authenticating user's recent Tweets. Any attempt that would result in duplication will be blocked, resulting in a 403 error. A user cannot submit the same status twice in a row.

While not rate limited by the API, a user is limited in the number of Tweets they can create at a time. If the number of updates posted by the user reaches the current allowed limit this method will return an HTTP 403 error.

**About Geo**

* Any geo-tagging parameters in the update will be ignored if `geo_enabled` for the user is false (this is the default setting for all users, unless the user has enabled geolocation in their settings)
* The number of digits after the decimal separator passed to `lat` (up to 8) is tracked so that when the `lat` is returned in a status object it will have the same number of digits after the decimal separator.
* Use a decimal point as the separator (and not a decimal comma) for the latitude and the longitude - usage of a decimal comma will cause the geo-tagged portion of the status update to be dropped.
* For JSON, the response mostly uses conventions described in [GeoJSON](http://geojson.org/). However, the `geo` object coordinates that Twitter renders are **reversed** from the GeoJSON specification. GeoJSON specifies a longitude then a latitude, whereas Twitter represents it as a latitude then a longitude: `"geo": { "type":"Point", "coordinates":[37.78217, -122.40062] }`
* The `coordinates` object is replacing the `geo` object (no deprecation date has been set for the `geo` object yet) -- the difference is that the coordinates object, in JSON, is now rendered correctly in GeoJSON.
* If a `place_id` is passed into the status update, then that place will be attached to the status. If no `place_id` was explicitly provided, but `latitude` and `longitude` are, the API attempts to implicitly provide a place by calling [geo/reverse\_geocode](https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-reverse_geocode).
* Users have the ability to remove all geotags from all their Tweets en masse via the user settings page. Currently there is no method to remove geotags from individual Tweets.