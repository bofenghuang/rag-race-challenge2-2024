platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids


## Parameters[¶](#parameters "Permalink to this headline")

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| id  | required | The numerical ID of the desired status. |     | `327473909412814850` |
| count | optional | Specifies the number of records to retrieve. Must be less than or equal to 100. |     | `5` |
| cursor | semi-optional | Causes the list of IDs to be broken into pages of no more than 100 IDs at a time. The number of IDs returned is not guaranteed to be 100 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [our cursor docs](https://developer.twitter.com/en/docs/basics/cursoring) for more information.<br><br>While this method supports the cursor parameter, the entire result set can be returned in a single cursored collection. Using the `count` parameter with this method will not provide segmented cursors for use with this parameter. |     | `12893764510938` |
| stringify\_ids | optional | Many programming environments will not consume Tweet ids due to their size. Provide this option to have ids returned as strings instead. |     | `true` |