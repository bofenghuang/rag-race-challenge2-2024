platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate/standard-to-twitter-api-v2


### Similarities

#### Request parameters and operators

The standard v1.1 statuses/filter endpoint features a few parameters that can be passed along with the request to filter the stream. With v2 filtered stream, you instead use a set of [operators](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule) that can be connected together using boolean logic to filter for desired Tweets. The available operators include some that are direct replacements for the existing standard v1.1 parameters. 

The following standard v1.1 request parameters have equivalent operators in Twitter API v2:  
 

| **Standard** | **Twitter API v2** |
| --- | --- |
| follow - A comma-separated list of user IDs, indicating the users whose Tweets should be delivered on the stream. | Many operators that can help you find Tweets related to specific users:<br><br>* @<br>* from:<br>* to:<br>* etc. |
| track - A comma-separated list of phrases which will be used to determine what Tweets will be delivered on the stream. | Many operators that can help you find Tweets related to specific keywords:<br><br>* keyword<br>* "exact phrase match"<br>* #<br>* etc. |

**Support for Tweet edit history and metadata**  

Both versions provide metadata that describes any edit history. Check out the [filtered stream API References](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference) and the [Tweet edits fundamentals page](https://developer.twitter.com/en/docs/twitter-api/tweet-edits) for more details.