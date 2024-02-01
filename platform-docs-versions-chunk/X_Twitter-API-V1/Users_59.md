platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy

POST mutes/users/destroy

post-mutes-users-destroy

# POST mutes/users/destroy

Un-mutes the user specified in the ID parameter for the authenticating user.

Returns the unmuted user when successful. Returns a string describing the failure condition when unsuccessful.

Actions taken in this method are asynchronous. Changes will be eventually consistent.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/mutes/users/destroy.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |