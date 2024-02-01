platform: X
topic: Twitter-API-V1
subtopic: Trends
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Trends.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/trends/locations-with-trending-topics/api-reference/get-trends-available

GET trends/available

get-trends-available

# GET trends/available

Returns the locations that Twitter has trending topic information for.

The response is an array of "locations" that encode the location's `WOEID` and some other human-readable information such as a canonical name and country the location belongs in.

Note: This endpoint uses the "where on earth identifier" or WOEID, which is a legacy identifier created by Yahoo and has been deprecated. Twitter API v1.1 still uses the numeric value to identify town and country trend locations. Reference our legacy [blog post](https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html) for more details. The url returned in the response, `where.yahooapis.com` is no longer valid.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/trends/available.json`