platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-show

## Example Response[¶](#example-response "Permalink to this headline")

    {
      "relationship": {
        "source": {
          "id": 783214,
          "id_str": "783214",
          "screen_name": "Twitter",
          "following": true,
          "followed_by": true,
          "live_following": false,
          "following_received": null,
          "following_requested": null,
          "notifications_enabled": null,
          "can_dm": true,
          "blocking": null,
          "blocked_by": null,
          "muting": null,
          "want_retweets": null,
          "all_replies": null,
          "marked_spam": null
        },
        "target": {
          "id": 2244994945,
          "id_str": "2244994945",
          "screen_name": "TwitterDev",
          "following": true,
          "followed_by": true,
          "following_received": null,
          "following_requested": null
        }
      }
    }