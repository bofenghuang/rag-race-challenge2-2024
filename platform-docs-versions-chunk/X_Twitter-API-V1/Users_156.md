platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-subscriptions


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. |     |     |
| screen\_name | optional | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     |     |
| count | optional | The amount of results to return per page. Defaults to 20. No more than 1000 results will ever be returned in a single page. |     |     |
| cursor | optional | Breaks the results into pages. Provide a value of _\-1_ to begin paging. Provide values as returned in the response body's _next\_cursor_ and _previous\_cursor_ attributes to page back and forth in the list. It is recommended to always use cursors when the method supports them. See [Cursoring](https://developer.twitter.com/en/docs/basics/cursoring) for more information. |     |     |