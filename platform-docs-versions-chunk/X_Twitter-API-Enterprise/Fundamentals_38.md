platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo

### Geo object data dictionary

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| coordinates | Collection of Float | The longitude and latitude of the Tweet’s location, as a collection in the form **\[latitude, longitude\]**. Example:<br><br>  **"geo": {**<br><br>    **"type":** "Point"**,**<br><br>    **"coordinates": \[**<br><br>      54.27784**,**<br><br>      \-0.41068<br><br>    **\]**<br><br>  **}** |
| type | String | The type of data encoded in the coordinates property. This will be “Point” for Tweet coordinates fields. Example:<br><br>"type": "Point" |