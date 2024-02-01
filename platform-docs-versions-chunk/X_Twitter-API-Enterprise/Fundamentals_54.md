platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities


### Poll object

The `entities` section will contain a `polls` array containing a single `poll` object if the Tweet contains a poll. If no poll is included, there will be no `polls` array in the `entities` section.

Note that these Poll metadata are only available with the following Enterprise APIs:

* Volume streams ([Decahose](https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/overview) )
* [Real-time PowerTrack](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview)
* [Historical PowerTrack](https://developer.twitter.com/en/docs/twitter-api/enterprise/historical-powertrack-api/overview)
* Twitter Search APIs ([Full-Archive Search](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview) and [30-Day Search](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview))

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| options | Array of Option Object | An array of options, each having a poll position, and the text for that position. Example:<br><br>{"options": \[<br>          {<br>            "position": 1,<br>            "text": "I read documentation once."<br>          }<br>      \]<br>} |
| end\_datetime | String | Time stamp (UTC) of when poll ends. Example:<br><br>"end\_datetime": "Thu May 25 22:20:27 +0000 2017" |
| duration\_minutes | String | Duration of poll in minutes. Example:<br><br>"duration\_minutes": 60 |