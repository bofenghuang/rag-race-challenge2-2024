platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-show

GET users/show

get-users-show

# GET users/show

Returns a [variety of information](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) about the user specified by the required `user_id` or `screen_name` parameter. The author's most recent Tweet will be returned inline when possible.

[GET users / lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) is used to retrieve a bulk collection of user objects.

You must be following a protected user to be able to see their most recent Tweet. If you don't follow a protected user, the user's Tweet will be removed. A Tweet will not always be returned in the current\_status field.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/users/show.json`