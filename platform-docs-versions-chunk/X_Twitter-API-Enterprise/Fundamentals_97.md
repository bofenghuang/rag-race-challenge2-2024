platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/gnip


### Data dictionary

|     |     |     |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| matching\_rules | array | Contains an array of matching rule objects which indicate the rule which the activity matches on.  <br>    **"matching\_rules": \[**<br><br>      **{**<br><br>        **"tag": null,**<br><br>        **"id":** 1026514022567358500**,**<br><br>        **"id\_str":** "1026514022567358464"<br><br>      **}**<br><br>    **\]** |
| urls | array | Contains an array of the links within the activity, and the expanded url metadata for the \*\*\*URL unwinding enrichement  <br>  <br>    **"urls": \[**<br><br>      **{**<br><br>        **"url":** "https://t.co/tGQqNxxyhU"**,**<br><br>        **"expanded\_url":** "https://www.youtube.com/channel/UCwUxW2CV2p5mzjMBqvqLzJA"**,**<br><br>        **"expanded\_status":** 200**,**<br><br>        **"expanded\_url\_title":** "Birdys Daughter"**,**<br><br>        **"expanded\_url\_description":** "Premium, single-origin, handpicked Jamaica Blue Mountain Coffee"<br><br>      **}**<br><br>    **\]** |
| profileLocations | array of location objects | Contains the derived location object from the Profile Geo enrichment  <br>  <br>    **"profileLocations": \[**<br><br>      **{**<br><br>        **"address": {**<br><br>          **"country":** "Canada"**,**<br><br>          **"countryCode":** "CA"**,**<br><br>          **"locality":** "Toronto"**,**<br><br>          **"region":** "Ontario"<br><br>        **},**<br><br>        **"displayName":** "Toronto, Ontario, Canada"**,**<br><br>        **"geo": {**<br><br>          **"coordinates": \[**<br><br>            \-79.4163**,**<br><br>            43.70011<br><br>          **\],**<br><br>          **"type":** "point"<br><br>        **},**<br><br>        **"objectType":** "place"<br><br>      **}**<br><br>    **\]**<br><br>  **}** |