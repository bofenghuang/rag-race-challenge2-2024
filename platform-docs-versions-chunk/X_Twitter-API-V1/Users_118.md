platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-update

## Example Response[¶](#example-response "Permalink to this headline")

    {
      "relationship": {
        "source": {
          "id": 63046977,
          "id_str": "63046977",
          "screen_name": "happycamper",
          "following": true,
          "followed_by": false,
          "live_following": false,
          "following_received": null,
          "following_requested": false,
          "notifications_enabled": false,
          "can_dm": false,
          "blocking": false,
          "blocked_by": false,
          "muting": false,
          "want_retweets": true,
          "all_replies": false,
          "marked_spam": false
        },
        "target": {
          "id": 2244994945,
          "id_str": "2244994945",
          "screen_name": "TwitterDev",
          "following": false,
          "followed_by": true,
          "following_received": false,
          "following_requested": null
        }
      }
    }