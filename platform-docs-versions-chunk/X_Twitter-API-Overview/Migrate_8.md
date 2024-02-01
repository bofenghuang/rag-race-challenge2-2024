platform: X
topic: Twitter-API-Overview
subtopic: Migrate
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Overview/Migrate.md
url: https://developer.twitter.com/en/docs/twitter-api/migrate/whats-new


### New metrics available within Tweets, users, Spaces, and media objects

More metrics are now accessible within Tweet, user, Spaces, Lists, and media objects. These metrics are both public and private, and some metrics can be broken down into an organic or promoted context for Tweet ads. 

Learn more about the available [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics).  
 

|     |     | All Tweets |     | Ads |     |
| --- | --- | --- | --- | --- | --- |
| **Object** | **Available metrics** | **Public metrics** | **Private metrics**  <br>(requires [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) auth) | **Organic metrics** | **Promoted metrics** |
| tweets | retweet\_count | ✔️  |     | ✔️  | ✔️  |
| quote\_count | ✔️  |     |     |     |
| like\_count | ✔️  |     | ✔️  | ✔️  |
| reply\_count | ✔️  |     | ✔️  | ✔️  |
| impression\_count |     | ✔️  | ✔️  | ✔️  |
| url\_profile\_clicks |     | ✔️  | ✔️  | ✔️  |
| url\_link\_clicks |     | ✔️  | ✔️  | ✔️  |
| user | follower\_count | ✔️  |     |     |     |
| following\_count | ✔️  |     |     |     |
| tweet\_count | ✔️  |     |     |     |
| listed\_count | ✔️  |     |     |     |
| media | view\_count |     | ✔️  |     |     |
| playback\_0\_count  <br>playback\_25\_count  <br>playback\_50\_count  <br>playback\_75\_count  <br>playback\_100\_count |     | ✔️  |     |     |
| space | participant\_count | ✔️  |     |     |     |
| subscriber\_count |     | ✔️  |     |     |
| list | follower\_count | ✔️  |     |     |     |
| member\_count | ✔️  |     |     |     |

      ` "public_metrics": {             "retweet_count": 5239,             "reply_count": 1844,             "like_count": 17168,             "quote_count": 3275         }     "non_public_metrics": {             "impression_count": 956,             "user_profile_clicks": 34,             "url_link_clicks": 57    }      "organic_metrics": {             "impression_count": 956,             "like_count": 1244,             "reply_count": 300,             "user_profile_clicks": 150             "url_link_clicks": 57         }      "promoted_metrics": {             "impression_count": 25086,             "like_count": 9045,             "reply_count": 637,             "user_profile_clicks": 265,             "url_link_clicks": 48         }`