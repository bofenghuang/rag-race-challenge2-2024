platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/get-collections-entries

GET collections/entries

get-collections-entries

# GET collections/entries

Retrieve the identified Collection, presented as a list of the Tweets curated within.

The response structure of this method differs significantly from timelines you may be used to working with elsewhere in the Twitter API.

To navigate a Collection, use the position object of a response, which includes attributes for `max_position`, `min_position`, and `was_truncated`. `was_truncated` indicates whether additional Tweets exist in the collection outside of the range of the current request. To retrieve Tweets further back in time, use the value of `min_position` found in the current response as the `max_position` parameter in the next call to this endpoint.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/collections/entries.json`