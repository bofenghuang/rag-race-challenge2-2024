platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-list

GET lists/list

get-lists-list

# GET lists/list

Returns all lists the authenticating or specified user subscribes to, including their own. The user is specified using the `user_id` or `screen_name` parameters. If no user is given, the authenticating user is used.

A maximum of 100 results will be returned by this call. Subscribed lists are returned first, followed by owned lists. This means that if a user subscribes to 90 lists and owns 20 lists, this method returns 90 subscriptions and 10 owned lists. The `reverse` method returns owned lists first, so with `reverse=true`, 20 owned lists and 80 subscriptions would be returned. If your goal is to obtain every list a user owns or subscribes to, use [GET lists / ownerships](https://developer.twitter.com/rest/reference/get/lists/ownerships) and/or [GET lists / subscriptions](https://developer.twitter.com/rest/reference/get/lists/subscriptions) instead.