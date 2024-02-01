platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-incoming

## Parameters[¶](#parameters "Permalink to this headline")

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| cursor | semi-optional | Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. |     | `12893764510938` |
| stringify\_ids | optional | Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. |     | `true` |

## Example Request[¶](#example-request "Permalink to this headline")

`GET https://api.twitter.com/1.1/friendships/incoming.json`