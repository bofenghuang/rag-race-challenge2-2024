platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/delete-users-source_id-following

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "following": false   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `following` | boolean | Indicates whether the source\_user\_id is unfollowing the specified user as a result of this request. This value is `false` for a successful the unfollow request. |