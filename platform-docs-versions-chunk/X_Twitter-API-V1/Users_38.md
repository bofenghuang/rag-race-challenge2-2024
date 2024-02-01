platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-blocks-ids

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/blocks/ids.json?stringify_ids=true&cursor=-1`

## Example Response[¶](#example-response "Permalink to this headline")

    {
      "ids": [
        "123"
      ],
      "next_cursor": 0,
      "next_cursor_str": "0",
      "previous_cursor": 0,
      "previous_cursor_str": "0"
    }