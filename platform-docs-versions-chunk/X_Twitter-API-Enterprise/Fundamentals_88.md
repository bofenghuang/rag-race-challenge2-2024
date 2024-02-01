platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/location


### Location data dictionary

| Field | Type | Description |
| --- | --- | --- |
| objectType | string | See [here](http://activitystrea.ms/head/activity-schema.html#place) for more detailed information. Example:<br><br>**"objectType":** "place" |
| displayName | string | **The full name of the location.  <br>  <br>****"displayName":** "United States" |
| name | string | Name of the location from Twitter's place JSON format. |
| link | string | A link to the full Twitter JSON representation of the place.  <br>  <br>**"link":** "https://api.twitter.com/1.1/geo/id/27c45d804c777999.json" |
| geo | object | The geo coordintates object from Twitter.  Either a polygon, or point.<br><br>See [geo](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/geo.html#coordinates) |
| countryCode | String | Shortened country code representing the country containing this place. Example:<br><br>**"countryCode": "US** |
| country | String | Name of the country containing this place. Example:<br><br>**"country":** "United States" |