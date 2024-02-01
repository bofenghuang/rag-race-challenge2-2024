platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/geo


### Bounding box[](#bounding-box "Permalink to this headline")

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| coordinates | Array of Array of Array of Float | A series of longitude and latitude points, defining a box which will contain the Place entity this bounding box is related to. Each point is an array in the form of \[longitude, latitude\]. Points are grouped into an array per bounding box. Bounding box arrays are wrapped in one additional array to be compatible with the polygon notation. Example:<br><br>{<br>  "coordinates": \[<br>    \[<br>      \[<br>        -74.026675,<br>        40.683935<br>      \],<br>      \[<br>        -74.026675,<br>        40.877483<br>      \],<br>      \[<br>        -73.910408,<br>        40.877483<br>      \],<br>      \[<br>        -73.910408,<br>        40.3935<br>      \]<br>    \]<br>  \]<br>} |
| type | String | The type of data encoded in the coordinates property. This will be “Polygon” for bounding boxes and “Point” for Tweets with exact coordinates. Example:<br><br>"type":"Polygon" |