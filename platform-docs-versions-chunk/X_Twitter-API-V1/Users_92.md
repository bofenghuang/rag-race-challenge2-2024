platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-no_retweets-ids

GET friendships/no\_retweets/ids

get-friendships-no\_retweets-ids

# GET friendships/no\_retweets/ids

Returns a collection of user\_ids that the currently authenticated user does not want to receive retweets from.

Use [POST friendships / update](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/post-friendships-update) to set the "no retweets" status for a given user account on behalf of the current user.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/friendships/no_retweets/ids.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |