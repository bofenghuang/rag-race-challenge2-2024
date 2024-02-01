platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place


## Place

The place tagged in a Tweet is not a primary object on any endpoint, but can be found and expanded in the Tweet resource. 

The object is available for expansion with `?expansions=geo.place_id` to get the condensed object with only default fields. Use the expansion with the field parameter: `place.fields` when requesting additional fields to complete the object.

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| full\_name (default) | string | A longer-form detailed place name.<br><br>`"full_name": "Manhattan, NY"` | Classify a Tweet by a specific place name |
| id (default) | string | The unique identifier of the expanded place, if this is a point of interest tagged in the Tweet.<br><br>`"id": "01a9a39529b27f36"` | Use this to programmatically retrieve a place |
| contained\_within | array | Returns the identifiers of known places that contain the referenced place. |     |
| country | string | The full-length name of the country this place belongs to.<br><br>`"country": "United States"` | Classify a Tweet by country name |
| country\_code | string | The ISO Alpha-2 country code this place belongs to.<br><br>`"country_code": "US"` | Classify a Tweet by country code |
| geo | object | Contains place details in GeoJSON format.<br><br>`"geo": {        "type": "Feature",        "bbox": [              -74.026675,              40.683935,              -73.910408,              40.877483         ],         "properties": {}      }` |     |
| name | string | The short name of this place.<br><br>`"name": "Manhattan"` | Classify a Tweet by a specific place name |
| place\_type | string | Specified the particular type of information represented by this place information, such as a city name, or a point of interest.<br><br>`"place_type": "city"` | Classify a Tweet by a specific type of place |