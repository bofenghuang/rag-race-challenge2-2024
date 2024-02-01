platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet

## Tweet Object

When using enterprise data products, you will notice that much of the data dictionary is similar to the native format of Tweet data, with some additional enriched metadata.  The base level of the native enriched format uses much of the same object names as the [Twitter API v1.1 data format](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/intro-to-tweet-json.html).  The Tweet object has a long list of ‘root-level’ attributes, including fundamental attributes such as `id`, `created_at`, and `text`. Tweet objects will also have nested objects to include the `user`, `entities`, and `extended_entities`. Tweet objects will also have other [nested Tweet objects](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/nested-tweet-objects) such as retweeted\_status, quoted\_status and extended\_tweet.  The native enriched format will additionally have a matching\_rules object.