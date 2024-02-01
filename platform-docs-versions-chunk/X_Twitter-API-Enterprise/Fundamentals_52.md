platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities


### User mention object  

The `entities` section will contain a `user_mentions` array containing an object for every user mention included in the Tweet body, and include an empty array if no user mention is present.

The PowerTrack `@` Operator is used to match on the `screen_name` attribute. The `has:mentions` Operator will match if there is at least one item in the array.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| id  | Int64 | ID of the mentioned user, as an integer. Example:<br><br>"id":6253282 |
| id\_str | String | If of the mentioned user, as a string. Example:<br><br>"id\_str":"6253282" |
| indices | Array of Int | An array of integers representing the offsets within the Tweet text where the user reference begins and ends. The first integer represents the location of the ‘@’ character of the user mention. The second integer represents the location of the first non-screenname character following the user mention. Example:<br><br>"indices":\[4,15\] |
| name | String | Display name of the referenced user. Example:<br><br>"name":"Twitter API" |
| screen\_name | String | Screen name of the referenced user. Example:<br><br>"screen\_name":"twitterapi" |