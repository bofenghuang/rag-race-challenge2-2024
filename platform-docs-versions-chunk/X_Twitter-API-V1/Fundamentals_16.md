platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/geo

## Introduction

Tweets can be associated with a location, generating a Tweet that has been ‘geo-tagged.’ Tweet locations can be assigned by using the Twitter user-interface or when posting a Tweet using the API. Tweet locations can be an exact ‘point’ location, or a Twitter Place with a ‘bounding box’ that describes a larger area ranging from a venue to an entire region.

There are two ‘root-level’ JSON objects used to describe the location associated with a Tweet: `coordinates` and `place`.

    {
       "coordinates": {}, 
       "place": {}
    }

The `place` object is always present when a Tweet is geo-tagged, while the `coordinates` object is only present (non-null) when the Tweet is assigned an _exact location_. If an exact location is provided, the `coordinates` object will provide a \[long, lat\] array with the geographical coordinates, and a Twitter Place that corresponds to that location will be assigned.