platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/activity


## Activity Object

Activity Streams is an object schema translation of Twitter's [original data format](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/intro-to-tweet-json) created by Gnip to 'normalize the format' of Tweet data and other social media data using the third party [Activity Base Schema described here](https://activitystrea.ms/head/activity-schema.html).  Tweets are normalized into the activity streams schema, including: note, person, place and service object types as nested objects.  Tweets can have other nested Tweet activity obejcts for Retweets, or others including twitter\_quoted\_status, long\_object.

The base level object type "activity" is similar to the [Tweet base level object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html) of the native enriched format.  Example payloads in activity streams format can be found [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/example-payloads.html).