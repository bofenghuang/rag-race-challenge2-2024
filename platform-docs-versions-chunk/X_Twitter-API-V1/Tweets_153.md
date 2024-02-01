platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/overview/response_structures

## Single objects

Even methods that return a single “primary object” respond with a decomposed structure, similar to a collection.

Methods that can return only one core object:

You will see responses like this in: [GET collections / show](https://dev.twitter.com/rest/reference/get/collections/show)

### Structure

response (object)

* a key/value pair indicating the object’s type and identifier (e.g. "timeline\_id":"custom-393773270547177472")

objects (object)

* users (object, ID as key)
* tweets (object, ID as key)
* timelines (object, ID as key)