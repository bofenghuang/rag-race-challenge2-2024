platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/fields

Fields

The Twitter API v2 endpoints are equipped with a set of parameters called _fields,_ which allows you to select just the data that you want from each of the objects in your endpoint response.

By default, the Tweet object only returns the id and the text fields, and for Tweets created since September 29, 2022, the edit\_history\_tweet\_ids field. If you need the Tweet’s created date or public metrics, you will need to use the tweet.fields parameters to request them. This provides a higher degree of customization by enabling you to only request the fields you require depending on your use case. For example, you would include this query string in your request 

?tweet.fields=created\_at,public\_metrics

Each object has its own parameter which is used to specifically request the fields that are associated with that object. Here are the different fields parameters that are currently available:  

* [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) → `tweet.fields`
* [User](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) → `user.fields`
* [Media](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) → `media.fields`
* [Poll](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll) → `poll.fields`
* [Place](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place) → `place.fields`

  
When using an endpoint that primarily returns a particular object, simply use the matching field parameter and specify the field(s) desired in a comma-separated list as the value to that parameter to retrieve those fields in the response.