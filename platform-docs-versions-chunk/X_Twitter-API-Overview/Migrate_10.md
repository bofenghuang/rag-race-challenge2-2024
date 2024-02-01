platform: X
topic: Twitter-API-Overview
subtopic: Migrate
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Overview/Migrate.md
url: https://developer.twitter.com/en/docs/twitter-api/migrate/whats-new


### Connection Status

X API v2 now includes a feature that allows developers to lookup the relationship (called connection status) between the authenticating user and the user being looked up in the response payload.

This is comparable to [GET friendships/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-show) and [GET friendships/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-lookup) endpoints in V1.1. 

The sample API Request to get the connection status using the [User Lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction) Endpoint in the X API v2 is:

      `https://api.twitter.com/2/users/by/username/XDevelopers?user.fields=connection_status`
    

      `{     "data": {         "username": "XDevelopers",         "name": "Developers",         "connection_status": [             "following"         ],         "id": "2244994945"     } }`
    

Using the X API v2, a developer can programmatically find out if the authenticating user:

* is being followed by the user being looked up.
* is following the user being looked up.
* has received a follow request from the user being looked up.
* sent a follow request to the user being looked up.
* blocked the user being looked up.
* muted the user being looked up.