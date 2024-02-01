platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo


## Geo Objects

Tweets can be associated with a location, generating a Tweet that has been ‘geo-tagged.’ Tweet locations can be assigned by using the Twitter user-interface or when posting a Tweet using the API. Tweet locations can be an exact ‘point’ location, or a Twitter Place with a ‘bounding box’ that describes a larger area ranging from a venue to an entire region.

There are three ‘root-level’ JSON objects used to describe the location associated with a Tweet: [place](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/place-dictionary), [geo](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo) and [coordinates](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/coordinates). 

Additionally, the native enriched format includes the [profile geo enrichment's](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo.html) [derived location](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/derived-location) within the user object.

The `place` object is always present when a Tweet is geo-tagged with a place,. Places are specific, named locations with corresponding geo coordinates. When users decide to assign a location to their Tweet, they are presented with a list of candidate Twitter Places. When using the API to post a Tweet, a Twitter Place can be attached by specifying a place\_id when posting the Tweet. Tweets associated with Places are not necessarily issued from that location but could also potentially be _about_ that location.

The geo and `coordinates` objects only present (non-null) when the Tweet is assigned an _exact location_. If an exact location is provided, the `coordinates` object will provide a \[long, lat\] array with the geographical coordinates, and a Twitter Place that corresponds to that location will be assigned.