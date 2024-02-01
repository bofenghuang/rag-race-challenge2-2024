platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/overview/about_collections


## Working with the Collections API

Use these methods to browse Collections, whether by ID, those owned by a specific user, or those containing a specific Tweet.

* [GET collections / list](https://dev.twitter.com/rest/reference/get/collections/list)
* [GET collections / show](https://dev.twitter.com/rest/reference/get/collections/show)

These methods allow you to create, modify, or delete a collection on behalf of the currently authenticated user.

* [POST collections / create](https://dev.twitter.com/rest/reference/post/collections/create)
* [POST collections / destroy](https://dev.twitter.com/rest/reference/post/collections/destroy)
* [POST collections / update](https://dev.twitter.com/rest/reference/post/collections/update)

To curate a collection, add or remove Tweets with these methods:

* [GET collections / entries](https://dev.twitter.com/rest/reference/get/collections/entries)
* [POST collections / entries / add](https://dev.twitter.com/rest/reference/post/collections/entries/add)
* [POST collections / entries / remove](https://dev.twitter.com/rest/reference/post/collections/entries/remove)
* [POST collections / entries / move](https://dev.twitter.com/rest/reference/post/collections/entries/move)
* [POST collections / entries / curate](https://dev.twitter.com/rest/reference/post/collections/entries/curate)