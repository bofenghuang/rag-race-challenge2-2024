platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities


### URL object 

The `entities` section will contain a `urls` array containing an object for every link included in the Tweet body, and include an empty array if no links are present.

The `has:links` Operator will match if there is at least one item in the array. The `url:` Operator is used to match on the `expanded_url` attribute. If you are using the [Expanded URL enrichment](http://support.gnip.com/enrichments/expanded_urls.html), the `url:` Operator is used to match on the `unwound.url` (fully unwound URL) attribute. If you are using the [Exhanced URL enrichment](http://support.gnip.com/enrichments/enhanced_urls.html), the `url_title:` and `url_decription:` Operators are used to match on the `unwound.title` and `unwound.description` attributes.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| display\_url | String | URL pasted/typed into Tweet. Example:<br><br>"display\_url":"bit.ly/2so49n2" |
| expanded\_url | String | Expanded version of \`\` display\_url\`\` . Example:<br><br>"expanded\_url":"http://bit.ly/2so49n2" |
| indices | Array of Int | An array of integers representing offsets within the Tweet text where the URL begins and ends. The first integer represents the location of the first character of the URL in the Tweet text. The second integer represents the location of the first non-URL character after the end of the URL. Example:<br><br>"indices":\[30,53\] |
| url | String | Wrapped URL, corresponding to the value embedded directly into the raw Tweet text, and the values for the indices parameter. Example:<br><br>"url":"https://t.co/yzocNFvJuL" |

If you are using the Expanded and/or Enhanced URL enrichments, the following metadata is available under the `unwound` attribute:

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| url | String | The fully unwound version of the link included in the Tweet. Example:<br><br>"url":"https://blog.twitter.com/en\_us/topics/insights/2016/using-twitter-as-a-go-to-communication-channel-during-severe-weather-events.html" |
| status | Int | Final HTTP status of the unwinding process, a '200' indicating success. Example:<br><br>200 |
| title | String | HTML title for the link. Example:<br><br>"title":"Using Twitter as a ‘go-to’ communication channel during severe weather" |
| description | String | HTML description for the link. Example:<br><br>"description":"Using Twitter as a ‘go-to’ communication channel during severe weather" |