platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids

GET followers/ids

get-followers-ids

# GET followers/ids

Returns a cursored collection of user IDs for every user following the specified user.

At this time, results are ordered with the most recent following first — however, this ordering is subject to unannounced change and eventual consistency issues. Results are given in groups of 5,000 user IDs and multiple "pages" of results can be navigated through using the `next_cursor` value in subsequent requests. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information.

This method is especially powerful when used in conjunction with [GET users / lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup), a method that allows you to convert user IDs into full [user objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) in bulk.