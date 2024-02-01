platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-ids

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/mutes/users/ids.json?cursor=-1`

## Example Response[¶](#example-response "Permalink to this headline")

    {
      "ids": [
        1228026486,
        54931584
      ],
      "next_cursor": 0,
      "next_cursor_str": "0",
      "previous_cursor": 0,
      "previous_cursor_str": "0"
    }