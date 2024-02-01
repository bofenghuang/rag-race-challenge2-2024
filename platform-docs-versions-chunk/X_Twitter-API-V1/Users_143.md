platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-statuses

GET lists/statuses

get-lists-statuses

# GET lists/statuses

Returns a timeline of tweets authored by members of the specified list. Retweets are included by default. Use the `include_rts=false` parameter to omit retweets.

[Embedded Timelines](https://developer.twitter.com/web/embedded-timelines) is a great way to embed list timelines on your website.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/lists/statuses.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 900 |