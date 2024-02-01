platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/geo


## Place data dictionary

| Field | Type | Description |
| --- | --- | --- |
| id  | String | ID representing this place. Note that this is represented as a string, not an integer. Example:<br><br>"id":"01a9a39529b27f36" |
| url | String | URL representing the location of additional place metadata for this place. Example:<br><br>"url":"https://api.twitter.com/1.1/geo/id/01a9a39529b27f36.json" |
| place\_type | String | The type of location represented by this place. Example:<br><br>"place\_type":"city" |
| name | String | Short human-readable representation of the place’s name. Example:<br><br>"name":"Manhattan" |
| full\_name | String | Full human-readable representation of the place’s name. Example:<br><br>"full\_name":"Manhattan, NY" |
| country\_code | String | Shortened country code representing the country containing this place. Example:<br><br>"country\_code":"US" |
| country | String | Name of the country containing this place. Example:<br><br>"country":"United States" |
| bounding\_box | [Object](#obj-boundingbox) | A bounding box of coordinates which encloses this place. Example:<br><br>{<br>  "bounding\_box": {<br>    "coordinates": \[<br>      \[<br>        \[<br>          -74.026675,<br>          40.683935<br>        \],<br>        \[<br>          -74.026675,<br>          40.877483<br>        \],<br>        \[<br>          -73.910408,<br>          40.877483<br>        \],<br>        \[<br>          -73.910408,<br>          40.3935<br>        \]<br>      \]<br>    \],<br>    "type": "Polygon"<br>  }<br>} |
| attributes | Object | When using PowerTrack, 30-Day and Full-Archive Search APIs, and Volume Streams this hash is null. Example:<br><br>"attributes": {} |