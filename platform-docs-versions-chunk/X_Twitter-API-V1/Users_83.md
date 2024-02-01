platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-list


## Parameters[¶](#parameters "Permalink to this headline")

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| user\_id | optional | The ID of the user for whom to return results. |     | `12345` |
| screen\_name | optional | The screen name of the user for whom to return results. |     | `noradio` |
| cursor | semi-optional | Causes the results to be broken into pages. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. | `-1` | `12893764510938` |
| count | optional | The number of users to return per page, up to a maximum of 200. | `20` | `42` |
| skip\_status | optional | When set to either `true`, `t` or `1` statuses will not be included in the returned user objects. | `false` | `false` |
| include\_user\_entities | optional | The user object `entities` node will not be included when set to `false`. | `true` | `false` |