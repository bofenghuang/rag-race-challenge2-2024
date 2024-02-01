platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/location


## profileLocations derived obejcts

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| address | object | Within profileLocation location object within the [gnip object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/gnip.html).  Address of location derived by the [profile geo enrichement](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo.html).  Level of granularity will vary. <br><br>**"address": {**<br><br>          **"country":** "United States"**,**<br><br>          **"countryCode":** "US"**,**<br><br>          **"locality":** "Providence"**,**<br><br>          **"region":** "Rhode Island"**,**<br><br>          **"subRegion":** "Providence County"<br><br>        **}** |
| geo | object | Within profileLocation location object within the [gnip objec](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/gnip.html)t. Centroid coordinates of the location derived by the [profile geo enrichement](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo.html).<br><br>**"geo": {**<br><br>          **"coordinates": \[**<br><br>            \-98.5**,**<br><br>            39.76<br><br>          **\],**<br><br>          **"type":** "point"<br><br>        **}** |