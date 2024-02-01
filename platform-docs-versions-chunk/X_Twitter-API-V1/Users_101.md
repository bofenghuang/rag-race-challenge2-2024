platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup


# GET users/lookup

Returns fully-hydrated [user objects](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) for up to 100 users per request, as specified by comma-separated values passed to the `user_id` and/or `screen_name` parameters.

This method is especially useful when used in conjunction with collections of user IDs returned from [GET friends / ids](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids) and [GET followers / ids](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids).

[GET users / show](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show) is used to retrieve a single user object.

There are a few things to note when using this method.

* You must be following a protected user to be able to see their most recent status update. If you don't follow a protected user their status will be removed.
* The order of user IDs or screen names may not match the order of users in the returned array.
* If a requested user is unknown, suspended, or deleted, then that user will not be returned in the results list.
* If none of your lookup criteria can be satisfied by returning a user object, a HTTP 404 will be thrown.
* You are strongly encouraged to use a POST for larger requests.