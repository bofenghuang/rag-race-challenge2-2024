platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities

## Entities object

The `entities` and `extended_entities` sections are both made up of arrays of entity _objects_. Below you will find descriptions for each of these entity objects, including data dictionaries that describe the object attribute names, types, and short description. We’ll also indicate which PowerTrack Operators match these attributes, and include some sample JSON payloads.

A collection of common entities found in Tweets, including hashtags, links, and user mentions. This `entities` object does include a `media` attribute, but its implementation in the `entiites` section is only completely accurate for Tweets with a single photo. For all Tweets with more than one photo, a video, or animated GIF, the reader is directed to the `extended_entities` section.