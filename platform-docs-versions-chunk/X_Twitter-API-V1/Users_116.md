platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-update

POST friendships/update

post-friendships-update

# POST friendships/update

Turn on/off Retweets and device notifications from the specified user.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/friendships/update.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the user being followed. |     | _twitterdev_ |
| user\_id | optional | The ID of the user being followed. |     | _2244994945_ |
| device | optional | Turn on/off device notifications from the target user. |     | _true_ |
| retweets | optional | Turn on/off Retweets from the target user. |     | _false_ |