platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/overview/response_structures

## Object collections

API methods that return multiple objects of the same type are segmented such that one component of the response contains the objects and any associated objects while another component simply lists references to those same objects and contextual information (such as cursors) needed to navigate the boundaries of the collection in subsequent requests.

You will see responses like this in [GET collections / list](https://dev.twitter.com/rest/reference/get/collections/list).

### Structure

* response (object)
    * results (array of objects)
        * each object typically contains one key/value pair housing an object’s ID
    * cursors (object)
        * next\_cursor (string)
        * previous\_cursor (string)
* objects (object)
    * users (object, ID as key)
    * tweets (object, ID as key)
    * timelines (object, ID as key)