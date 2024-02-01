platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities

### Symbol object  

The `entities` section will contain a `symbols` array containing an object for every $cashtag included in the Tweet body, and include an empty array if no symbol is present.

The PowerTrack `$` Operator is used to match on the `text` attribute. The `has:symbols` Operator will match if there is at least one item in the array.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| indices | Array of Int | An array of integers indicating the offsets within the Tweet text where the symbol/cashtag begins and ends. The first integer represents the location of the $ character in the Tweet text string. The second integer represents the location of the first character after the cashtag. Therefore the difference between the two numbers will be the length of the hashtag name plus one (for the ‘$’ character). Example:<br><br>"indices":\[12,17\] |
| text | String | Name of the cashhtag, minus the leading ‘$’ character. Example:<br><br>"text":"twtr" |