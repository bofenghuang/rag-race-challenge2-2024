platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/standard-operators


## Additional parameters

There is a set of additional parameters that allows a better control of the search results. The [standard search API reference](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/search/api-reference/get-search-tweets) documentation has detailed information about the usage of the parameters, this section will only give a brief description of their capabilities:

* **Result Type**: just like twitter.com/search results, the result\_type parameter selects whether the result set will be represented by recent or popular Tweets, or even a mix of both.
* **Geolocalization**: the search operator “near” isn’t available in the API, but there is a more precise way to restrict your query by a given location using the geocode parameter specified with the template “latitude,longitude,radius”, for example, “37.781157,-122.398720,1mi”. When conducting geo searches, the search API will first attempt to find Tweets which have lat/long within the queried geocode, and in case of not having success, it will attempt to find Tweets created by users whose profile location can be reverse geocoded into a lat/long within the queried geocode, meaning that is possible to receive Tweets which do not include lat/long information.
* **Language**: the lang parameter restricts Tweets to the given language.
* **Iterating in a result set**: parameters such count, until, since\_id, max\_id control iteration through search results, since it could be a large set of Tweets. The [Working with Timelines](https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines.html) documentation is a rich and illustrative tutorial to learn how to use these parameters to achieve the best efficiency and reliability when processing result sets.