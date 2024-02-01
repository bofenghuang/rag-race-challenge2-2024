platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate/powertrack-api-migration-to-twitter-api-v2


### Similarities

#### Streaming delivery method

Both PowerTrack and Twitter API v2 filtered stream use streaming data delivery, which require the client to establish an open connection to an endpoint and keeping a very long lived HTTP request, and parsing the response incrementally from the server in real time.  Both PowerTrack and Twitter API v2 filtered stream filter publicly available Tweets matching rules that exist on the stream in real time, and use keep-alive signals as new line characters (\\r\\n) to signal the connection is still active. Both PowerTrack and Twitter API v2 filtered stream endpoint connections deliver data in real time and should be read by the connecting client quickly.  

#### Integration process

Integrating with filtered stream is similar to integrating with PowerTrack, using the general process below:

1. Establish a streaming connection.
2. Asynchronously send separate requests to add and delete rules from the stream.
3. Reconnect to the stream automatically when connection is disconnected.

#### Persistent stream connection with separate rules management endpoints

Similar to the PowerTrack API and Rules API, the new Twitter API v2 filtered stream endpoints allows you to apply multiple rules to a single stream and add and remove rules to your stream while maintaining the stream connection.

|     |     |     |
| --- | --- | --- |
| **Feature** | **PowerTrack API** | **Twitter API v2 filtered stream** |
| **Connection endpoint** | [GET /stream](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-stream.html) | [GET /2/tweets/search/stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream.html) |
| **Add rules** | [POST /rules](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules.html#AddRules) | [POST /2/tweets/search/stream/rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules.html) |
| **Get rules** | [GET /rules](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules.html#ListRules) | [GET /2/tweets/search/stream/rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream-rules.html) |
| **Delete rules** | [POST /rules\_method=delete](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules.html#DeleteRules) | [POST /2/tweets/search/stream/rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules.html) |

#### Rule syntax, operators, and matching rules logic

The Twitter API v2 filtered stream uses a subset of the same rule operators currently used for PowerTrack rules. These operators are used to create boolean based rule syntax used for filtering desired matching Tweets from the live stream.  Both PowerTrack and filtered stream use the same rule syntax for building rules and matching logic is the same. While the majority of the operators are available for both PowerTrack and filter stream, there are a few notable differences and net new operators listed below.  For more details and example uses for each operator see current [PowerTrack operators](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/operators.html) and current Twitter API v2 [filtered stream operators](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule.html). 

Please note that many operators (noted as 'advanced operators') are reserved for those users who have been approved for [Academic Research access or Enterprise access](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level).

Operators available with both PowerTrack and Twitter API v2 Filter stream:

| **Standalone operators** | **Conjunction required operators (must be used with at least one standalone operator within a rule)** |
| --- | --- |
| keyword (example: coffee )<br><br>emoji (example: 🐶 or \\uD83D\\uDC36 )<br><br>"exact phrase match" (example: "happy birthday" )<br><br>from:<br><br>to:<br><br>@<br><br>retweets\_of:<br><br>#<br><br>url: | has:links<br><br>lang:<br><br>has:mentions<br><br>has:media<br><br>has:images<br><br>has:videos<br><br>is:retweet<br><br>is:quote<br><br>is:verified<br><br>has:hashtags<br><br>has:geo<br><br>sample:<br><br>\-is:nullcast |

|     |
| --- |
| **Net new operators available with Twitter API v2 filtered stream** |
| conversation\_id: - matches on Tweets that exist in any reply threads from the specified Tweet conversation root.Net new operators available with Twitter API v2 filtered stream:<br><br>context: - matches on Tweets that have been annotated with a context of interest. <br><br>entity: - matches on Tweets that have been annotated with an entity of interest. |

|     |
| --- |
| **Operators currently only available on PowerTrack API** |
| url\_title:<br><br>url\_description:<br><br>followers\_count:<br><br>statuses\_count:<br><br>friends\_count:<br><br>listed\_count:<br><br>"proximity match"~3<br><br>contains:<br><br>has:symbols<br><br>url\_contains:<br><br>in\_reply\_to\_status\_id:<br><br>retweets\_of\_status\_id:<br><br>source:<br><br>bio:<br><br>bio\_name:<br><br>bio\_location:<br><br>place:<br><br>place\_country:<br><br>point\_radius:<br><br>bounding\_box:<br><br>is:reply<br><br>(Available without conjunction)<br><br>has:links<br><br>lang:<br><br>has:mentions<br><br>has:media<br><br>has:images<br><br>has:videos<br><br>is:retweet<br><br>is:quote<br><br>is:verified<br><br>is:reply<br><br>has:hashtags<br><br>has:geo<br><br>sample: |

**Support for Tweet edit history and metadata**  

Both versions provide metadata that describes any edit history. Check out the [filtered stream API References](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference) and the [Edit Tweets fundamentals page](https://developer.twitter.com/en/docs/twitter-api/edit-tweets) for more details.