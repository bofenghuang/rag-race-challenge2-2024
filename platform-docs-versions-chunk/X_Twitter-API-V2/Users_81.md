platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/post-users-source_user_id-following

### Example responses

* [Successful response (public user)](#tab0)
* [Successful response (protected user)](#tab1)

Successful response (public user)

Successful response (protected user)

      `{   "data": {     "following": true,     "pending_follow": false   } }`
    

      `{   "data": {     "following": false,     "pending_follow": true   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `following` | boolean | Indicates whether the `id` is following the specified user as a result of this request. This value is `false` if the target user does not have public Tweets, as they will have to approve the follower request. |
| `pending_follow` | boolean | Indicates whether the target user will need to approve the follow request. Note that the authenticated user will follow the target user only when they approve the incoming follower request. |