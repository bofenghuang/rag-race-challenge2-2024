platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/migrate


### User Tweet timeline

The following tables compare the standard v1.1 and Twitter API v2 user Tweet timeline endpoints:

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Documentation | [API Reference](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline.html) | [API Reference](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-tweets.html) |
| HTTP methods supported | GET | GET |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint paths | /1.1/statuses/user\_timeline.json | /2/users/:id/tweets |
| Required parameters | user\_id or screen\_name | User ID set as path parameter :id |
| Authentication | OAuth 1.0a User Context<br><br>OAuth 2.0 App-Only | OAuth 1.0a User Context<br><br>OAuth 2.0 App-Only<br><br>OAuth 2.0 Authorization Code with PKCE |
| Request rate limits/Volume limits | 900 requests per 15 min with OAuth 1.0a User Context<br><br>1500 requests per 15 min with OAuth 2.0 App-Only<br><br>Request cap: 100,000 within a 24 hour period. | 900 requests per 15-minute window with OAuth 1.0a User Context<br><br>1500 requests per 15-minute window with OAuth 2.0 App-Only<br><br>[Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps):  <br>500,000 when using Essential access  <br>2 million when using Elevated access  <br>10 million when using Academic Research access |
| Default Tweets per response | 15  | 10  |
| Maximum Tweets per response | 200 | 100 |
| Historical Tweets available | The most recent 3,200 Tweets, including Retweets | The most recent 3,200 Tweets, including Retweets |
| Timeline navigation options | since\_id (exclusive) used for update polling<br><br>max\_id (inclusive) | start\_time<br><br>end\_time<br><br>since\_id (exclusive) used for update polling <br><br>until\_id (exclusive) |
| Optional parameters for results refinement | count  <br>exclude\_replies  <br>include\_rts  <br>trim\_user  <br>tweet\_mode  <br>since\_id  <br>max\_id | max\_results  <br>exclude(retweets,replies)  <br>tweet.fields  <br>user.fields  <br>place.fields  <br>media.fields  <br>poll.fields  <br>expansions  <br>start\_time  <br>end\_time  <br>since\_id  <br>until\_id |
| Supports requesting and receiving [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) | N/A | Returns Tweet results with inferred annotation data based on the Tweet text, such as 'Music Genre' and 'Folk Music' or 'Musician' and 'Dolly Parton' |
| Supports requesting and receiving specific Tweet [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) | N/A | Returns Tweet results with available public\_metrics per Tweet including retweet\_count, reply\_count, quote\_count and like\_count.  <br>  <br>Available with OAuth1.0a User Context:  <br>Additional non\_public\_metrics , including impression\_count, user\_profile\_clicks, url\_link\_clicks.<br><br>Additional media metrics such as view\_count and video playback metrics.<br><br>Additional organic\_metrics and promoted\_metrics available with OAuth 1.0a User Context for promoted Tweets. |
| Supports requesting and receiving [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id.html) | N/A | Returns a conversation\_id field where the value represents the first published Tweet in a reply thread to help you track conversations. |
| Tweet JSON format | [Standard v1.1 data format](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview.html) | [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/data-dictionary) format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Results order | Reverse chronological | Reverse chronological |
| Results pagination | N/A must use navigation by Tweet ID | Results can be reviewed moving forward or backward using a pagination\_token |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |
| Provides Tweet edit history | ✔   | ✔   |