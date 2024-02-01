platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo


### Introduction

Many Twitter user profiles include public location information provided by the user. This data is returned as a normal string in user.location (see [User object data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-object/user.html)). The Profile Geo Enrichment adds structured geodata relevant to the user.location value by geocoding and normalizing location strings where possible. Both latitude/longitude coordinates and related place metadata are added to user.derived.locations _only_ when included as part of the Tweet payload in enterprise API products. This data is available when using [the enriched native format](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/overview.html) and can be filtered with a combination of [PowerTrack rules](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/enterprise-operators).  

**Note:** Some of the supporting geodata used to create the Profile Geo enrichment comes from GeoNames.org and is used by Twitter under the [Creative Commons Attribution 3.0 License](https://creativecommons.org/licenses/by/3.0/us/legalcode).

Profile Geo data will be included in Twitter's PowerTrack, Replay, Volume Stream, Search, and Historical PowerTrack APIs.