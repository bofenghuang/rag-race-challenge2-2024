platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets_of_me


## Example Response[¶](#example-response "Permalink to this headline")

    [
      {
        "created_at": "Thu Nov 29 17:13:16 +0000 2018",
        "id": 1068191175616720896,
        "id_str": "1068191175616720896",
        "text": "@TwitterDev is the source of Twitter Developer news",
        "truncated": false,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [
            {
              "screen_name": "twitterdev",
              "name": "twitterdev",
              "id": 2244994945,
              "id_str": "2244994945",
              "indices": [
                0,
                10
              ]
            }
          ],
          "urls": []
        },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": 2244994945,
        "in_reply_to_user_id_str": "2244994945",
        "in_reply_to_screen_name": "twitterdev",
        "user": {
          "id": 10183220897015316771,
          "id_str": "10183220897015316771",
          "name": "test account",
          "screen_name": "testuser",
          "location": "USA",
          "description": "",
          "url": null,
          "entities": {
            "description": {
              "urls": []
            }
          },
          "protected": false,
          "followers_count": 3,
          "friends_count": 11,
          "listed_count": 0,
          "created_at": "Sun May 15 02:31:20 +0000 2019",
          "favourites_count": 33,
          "utc_offset": null,
          "time_zone": null,
          "geo_enabled": null,
          "verified": false,
          "statuses_count": 164,
          "lang": "null",
          "contributors_enabled": null,
          "is_translator": null,
          "is_translation_enabled": null,
          "profile_background_color": "null",
          "profile_background_image_url": null,
          "profile_background_image_url_https": null,
          "profile_background_tile": null,
          "profile_image_url": "null",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/1099410185435734016/G0hE-4u9_normal.jpg",
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/1018322089701531651/1539492123",
          "profile_link_color": "null",
          "profile_sidebar_border_color": "null",
          "profile_sidebar_fill_color": "null",
          "profile_text_color": "null",
          "profile_use_background_image": null,
          "has_extended_profile": null,
          "default_profile": true,
          "default_profile_image": false,
          "following": null,
          "follow_request_sent": null,
          "notifications": null,
          "translator_type": "null"
        },
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 1,
        "favorite_count": 1,
        "favorited": true,
        "retweeted": true,
        "lang": "en"
      }
    ]