platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/metrics


## Available Metrics

|     |     |     |
| --- | --- | --- |
| **Metric** | **API Representations** | **Description** |
| Impressions | `data.non_public_metrics.impression_count      data.organic_metrics.impression_count      data.promoted_metrics.impression_count` | A count of how many times the Tweet has been viewed (not unique by user). A view is counted if any part of the Tweet is visible on the screen.<br><br>This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.<br><br>Using the `non_public_metrics` field, this returns the total count of impressions from both organic and paid contexts.<br><br>Using the `organic_metrics` field, this returns the count of impressions from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the count of impressions from promoted contexts. |
| Retweets | `data.public_metrics.retweet_count      data.organic_metrics.retweet_count      data.promoted_metrics.retweet_count` | A count of how many times the Tweet has been Retweeted. Please note: This does not include Quote Tweets (“Retweets with comment”). To get the "Retweets and comments" total as displayed on the Twitter clients, simply add `retweet_count` and `quote_count`.<br><br>Using the `public_metrics` field, this will return the total count of Retweets from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.<br><br>Using the `organic_metrics` field, this returns the total count of Retweets from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the total count of Retweets from paid contexts. |
| Quote Tweets | `data.public_metrics.quote_count` | A count of how many times the Tweet has been Retweeted with a new comment (message). Please note: This does not include Retweets. To get the “Retweets and comments” total as displayed on the Twitter clients, simply add `retweet_count` and `quote_count`.<br><br>This will return the total count of Quote Tweets. There are no Quote Tweets from a paid context so all Quote Tweets are organic. |
| Likes | `data.public_metrics.like_count      data.organic_metrics.like_count      data.promoted_metrics.like_count` | A count of how many times the Tweet has been liked.<br><br>Using the `public_metrics` field, this will return the total count of likes from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.<br><br>Using the `organic_metrics` field, this returns the total count of Retweets from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the total count of Retweets from paid contexts. |
| Replies | `data.public_metrics.reply_count      data.organic_metrics.reply_count      data.promoted_metrics.reply_count` | A count of how many times the Tweet has been replied to.<br><br>Using the `public_metrics` field, this will return the total count of replies from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.<br><br>Using the `organic_metrics` field, this returns the total count of replies from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the total count of replies from paid contexts. |
| URL Link Clicks | `data.non_public_metrics.url_link_clicks      data.organic_metrics.url_link_clicks      data.promoted_metrics.url_link_clicks` | A count of the number of times a user clicks on a URL link or URL preview card in a Tweet.<br><br>This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.<br><br>Using the `non_public_metrics` field, this returns the total count of URL link clicks from both organic and paid contexts.<br><br>Using the `organic_metrics` field, this returns the count of URL link clicks from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the count of URL link clicks from paid contexts. |
| User Profile Clicks | `data.non_public_metrics.user_profile_clicks      data.organic_metrics.user_profile_clicks      data.promoted_metrics.user_profile_clicks` | A count of the number of times a user clicks the following portions of a Tweet: display name, user name, profile picture.<br><br>This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.<br><br>Using the `non_public_metrics` field, this returns the total count of user profile clicks from both organic and paid contexts.<br><br>Using the `organic_metrics` field, this returns the count of user profile clicks from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the count of user profile clicks from paid contexts. |
| Video views | `includes.media.public_metrics.view_count      includes.media.organic_metrics.view_count      includes.media.promoted_metrics.view_count` | A count of how many times the video included in the Tweet has been viewed.<br><br>This is the number of video views aggregated across all Tweets in which the given video has been posted. That means that the metric includes the combined views from any instance where the video has been Retweeted or reposted in separate Tweets.<br><br>Use expansion for media objects, `expansions=attachment.media_keys`.<br><br>Using the `public_metrics` field, this returns the total count of video views from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.<br><br>Using the `organic_metrics` field, this returns the total count of video views from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the total count of video views from paid contexts. |
| Video view quartiles | `includes.media.non_public_metrics.playback_0_count   includes.media.non_public_metrics.playback_25_count   includes.media.non_public_metrics.playback_50_count   includes.media.non_public_metrics.playback_75_count   includes.media.non_public_metrics.playback_100_count`<br><br>  <br><br>`includes.media.organic_metrics.playback_0_count   includes.media.organic_metrics.playback_25_count   includes.media.organic_metrics.playback_50_count   includes.media.organic_metrics.playback_75_count   includes.media.organic_metrics.playback_100_count`<br><br>  <br><br>`includes.media.promoted_metrics.playback_0_count   includes.media.promoted_metrics.playback_25_count   includes.media.promoted_metrics.playback_50_count   includes.media.promoted_metrics.playback_75_count   includes.media.promoted_metrics.playback_100_count   ` | The number of users who played through to each quartile in a video. This reflects the number of quartile views across all Tweets in which the given video has been posted.<br><br>This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.<br><br>Use expansion for media objects, `expansions=attachment.media_keys`.<br><br>Using the `non_public_metrics` field, this returns the total count of video view quartiles from both organic and paid contexts.<br><br>Using the `organic_metrics` field, this returns the total count of video view quartiles from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the total count of video view quartiles from paid contexts. |