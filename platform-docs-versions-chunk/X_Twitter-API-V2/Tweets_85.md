platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/migrate


### Reverse chronological home timeline

The following tables compare the standard v1.1 and Twitter API v2 home timeline endpoints:

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Documentation | [API Reference](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-home_timeline) | [API Reference](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-reverse-chronological.html.html) |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint paths | `/1.1/statuses/home_timeline.json` | `/2/users/:id/timelines/reverse_chronological` |
| Required parameters | `user_id` or `screen_name` | User ID set as path parameter :id |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>[OAuth 2.0 Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) |
| Request rate limits/Volume limits | 15 requests per 15-minute with OAuth 1.0a User Context<br><br>Request cap: 100,000 within a 24 hour period. | 180 requests per 15-minute window <br><br>[Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps):<br><br>500,000 when using Essential access<br><br>2 million when using Elevated access<br><br>10 million when using Academic Research access |
| Default Tweets per response | 15  | 100 |
| Maximum Tweets per response | 800 | This endpoint returns every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date. |
| Provides Tweet edit history | ✔   | ✔   |
| Historical Tweets available | The most recent 800 Tweets, including Retweets | The most recent 3,200 Tweets, including Retweets |
| Timeline navigation options | since\_id (exclusive) used for update polling<br><br>`max_id` (inclusive) | `start_time`<br><br>end\_time<br><br>`since_id`(exclusive) used for update polling <br><br>`until_id` (exclusive) |
| Optional parameters for results refinement | `count`<br><br>`exclude_replies`<br><br>`include_rts`<br><br>`trim_user`<br><br>`tweet_mode`<br><br>`since_id`<br><br>`max_id` | `max_results`<br><br>`exclude`(retweets,replies)<br><br>`tweet.fields`<br><br>`user.fields`<br><br>`place.fields`<br><br>`media.fields`<br><br>`poll.fields`<br><br>`expansions`<br><br>`start_time`<br><br>`end_time`<br><br>`since_id`<br><br>`until_id` |
| Supports requesting and receiving [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) | N/A | If annotations are included in tweet.fields, results will be annotated with inferred annotation data based on the Tweet text, such as 'Music Genre' and 'Folk Music' or 'Musician' and 'Dolly Parton' |
| Supports requesting and receiving specific Tweet [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) | N/A | If annotations are included in `tweet.fields`, results will be annotated with public\_metrics per Tweet including `retweet_count`, `reply_count`, `quote_count` and `like_count`, `non_public_metrics` , including `impression_count`, `user_profile_clicks`, `url_link_clicks`.<br><br>Additional media metrics such as view\_count and video playback metrics.<br><br>Additional organic\_metrics and promoted\_metrics available with User Context for promoted Tweets. |
| Supports requesting and receiving [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id.html) | N/A | Returns a conversation\_id field where the value represents the first published Tweet in a reply thread to help you track conversations. |
| Tweet JSON format | [Standard v1.1 data format](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview.html) | [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/data-dictionary) format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Results order | Reverse chronological | Reverse chronological |
| Results pagination | N/A must use navigation by Tweet ID | Results can be reviewed moving forward or backward using a pagination\_token |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |