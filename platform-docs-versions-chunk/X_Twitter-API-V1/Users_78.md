platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids


## Parameters[¶](#parameters "Permalink to this headline")

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| user\_id | optional | The ID of the user for whom to return results. |     | `12345` |
| screen\_name | optional | The screen name of the user for whom to return results. |     | `noradio` |
| cursor | semi-optional | Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. | `-1` | `12893764510938` |
| stringify\_ids | optional | Some programming environments will not consume Twitter IDs due to their size. Provide this option to have IDs returned as strings instead. More about [Twitter IDs](https://developer.twitter.com/en/docs/basics/twitter-ids). | `false` | `true` |
| count | optional | Specifies the number of IDs attempt retrieval of, up to a maximum of 5,000 per distinct request. The value of `count` is best thought of as a limit to the number of results to return. When using the count parameter with this method, it is wise to use a consistent count value across all requests to the same user's collection. Usage of this parameter is encouraged in environments where all 5,000 IDs constitutes too large of a response. |     | `2048` |