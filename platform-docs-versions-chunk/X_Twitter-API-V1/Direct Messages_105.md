platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/custom-profiles/api-reference/get-profile-list

## Example Response[¶](#example-response "Permalink to this headline")

    {
      "custom_profiles": [
        {
          "id": "100001",
          "created_timestamp": "1479767168196",
          "name": "Carol",
          "avatar": {
            "media": {
              "url": "https://pbs.twimg.com/some_img/987654321/ABC?format=jpg&name=normal"
            }
          }
        },
        {
          "id": "100002",
          "created_timestamp": "1479767168197",
          "name": "Andy",
          "avatar": {
            "media": {
              "url": "https://pbs.twimg.com/some_img/56565656/DEF?format=jpg&name=normal"
            }
          }
        }
     ],
     "next_cursor": "NDUzNDUzNDY3Nzc3"
    }