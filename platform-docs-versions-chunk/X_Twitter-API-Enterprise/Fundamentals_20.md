platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/overview

## Parsing best-practices

* Twitter JSON is encoded using UTF-8 characters.
* Parsers should tolerate variance in the ordering of fields with ease. It should be assumed that Tweet JSON is served as an unordered hash of data.
* Parsers should tolerate the addition of 'new' fields. 
* JSON parsers must be tolerant of ‘missing’ fields, since not all fields appear in all contexts.
* It is generally safe to consider a nulled field, an empty set, and the absence of a field as the same thing

### Next Steps:

* Review the enterprise [enriched native data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html)