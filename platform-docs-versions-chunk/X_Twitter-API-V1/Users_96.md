platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-outgoing

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/friendships/outgoing.json`

## Example Response[¶](#example-response "Permalink to this headline")

    {
      "previous_cursor": 0,
      "ids": [
        51937528,
        124856868,
        213246307,
        89356977,
        121177351,
        113338333,
        59520091,
        46451699,
        98223312,
        18172433,
        32210115,
        36851055,
        81269257
      ],
      "previous_cursor_str": "0",
      "next_cursor": 0,
      "next_cursor_str": "0"
    }