platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters


### locations

A comma-separated list of longitude,latitude pairs specifying a set of bounding boxes to filter Tweets by. Only geolocated Tweets falling within the requested bounding boxes will be included—unlike the Search API, the user’s location field is not used to filter Tweets.

Each bounding box should be specified as a pair of longitude and latitude pairs, with the southwest corner of the bounding box coming first. For example:

|     |     |
| --- | --- |
| Parameter value | Tracks Tweets from... |
| \-122.75,36.8,-121.75,37.8 | San Francisco |
| \-74,40,-73,41 | New York City |
| \-122.75,36.8,-121.75,37.8,-74,40,-73,41 | San FranciscoOR New York City |

Bounding boxes do not act as filters for other filter parameters. For example track=twitter&locations=-122.75,36.8,-121.75,37.8 would match any Tweets containing the term Twitter (even non-geo Tweets) OR coming from the San Francisco area.

The streaming API uses the following heuristic to determine whether a given Tweet falls within a bounding box:

* If the coordinates field is populated, the values there will be tested against the bounding box. Note that this field uses geoJSON order (longitude, latitude).
* If coordinates is empty but place is populated, the region defined in place is checked for intersection against the locations bounding box. Any overlap will match.
* If none of the rules listed above match, the Tweet does not match the location query. Note that the geo field is deprecated, and ignored by the streaming API.

If you would like to exclude place matches or only include places which fall completely within the bounding box, your code will have to perform an additional filtering step after reading the filtered stream.

Note that native Retweets are not matched by this parameter. While the original Tweet may have a location, the Retweet will not.