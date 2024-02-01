platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members


## Parameters[¶](#parameters "Permalink to this headline")

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| list\_id | required | The numerical `id` of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the `owner_id` or `owner_screen_name` parameters. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a `slug`. |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a `slug`. |     |     |
| count | optional | Specifies the number of results to return per page (see `cursor` below). The default is 20, with a maximum of 5,000. |     |     |
| cursor | semi-optional | Causes the collection of list members to be broken into "pages" of consistent sizes (specified by the `count` parameter). If no cursor is provided, a value of `-1` will be assumed, which is the first "page." |     |     |
| The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See Using cursors to navigate collections for more information. | `-1` | `12893764510938` |     |     |
| include\_entities | optional | The `entities` node will not be included when set to `false`. | `true` | `false` |
| skip\_status | optional | When set to either `true`, `t` or `1` statuses will not be included in the returned user objects. | `false` |     |