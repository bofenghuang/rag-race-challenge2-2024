platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-subscribers


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |
| count | optional | Specifies the number of results to return per page (see _cursor_ below). The default is 20, with a maximum of 5,000. |     |     |
| cursor | optional | Breaks the results into pages. A single page contains 20 lists. Provide a value of _\-1_ to begin paging. Provide values as returned in the response body's _next\_cursor_ and _previous\_cursor_ attributes to page back and forth in the list. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. |     |     |
| include\_entities | optional | When set to either _true_ , _t_ or _1_ , each tweet will include a node called "entities". This node offers a variety of metadata about the tweet in a discreet structure, including: user\_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See [Tweet Entities](https://developer.twitter.com/overview/api/tweets) for more details. |     |     |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user objects. |     |     |