platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-blocks-create

POST blocks/create

post-blocks-create

# POST blocks/create

Blocks the specified user from following the authenticating user. In addition the blocked user will not show in the authenticating users mentions or timeline (unless retweeted by another user). If a follow or friend relationship exists it is destroyed.

The URL pattern `/version/block/create/:screen_name_or_user_id.format` is still accepted but not recommended. As a sequence of numbers is a valid screen name we recommend using the `screen_name` or `user_id` parameter instead.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/blocks/create.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |