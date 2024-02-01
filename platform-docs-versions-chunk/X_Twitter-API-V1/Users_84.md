platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-list

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=twitterapi&skip_status=true&include_user_entities=false`

## Example Response[¶](#example-response "Permalink to this headline")

    {
    "users": [
          {user-object},
          {user-object},
          {user-object}
      ],
      "previous_cursor": 0,
      "previous_cursor_str": "0",
      "next_cursor": 1333504313713126852,
      "next_cursor_str": "1333504313713126852"
    }

For more detail, see the [user-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object).