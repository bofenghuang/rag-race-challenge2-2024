platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/entities

### Hashtag object  

The `entities` section will contain a `hashtags` array containing an object for every hashtag included in the Tweet body, and include an empty array if no hashtags are present.

The PowerTrack `#` Operator is used to match on the `text` attribute. The `has:hashtags` Operator will match if there is at least one item in the array.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| indices | Array of Int | An array of integers indicating the offsets within the Tweet text where the hashtag begins and ends. The first integer represents the location of the # character in the Tweet text string. The second integer represents the location of the first character after the hashtag. Therefore the difference between the two numbers will be the length of the hashtag name plus one (for the ‘#’ character). Example:<br><br>"indices":\[32,38\] |
| text | String | Name of the hashtag, minus the leading ‘#’ character. Example:<br><br>"text":"nodejs" |