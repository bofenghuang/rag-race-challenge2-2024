platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference

API reference

## API reference index

For the complete API reference, select an endpoint from the list.  
  

### Mutes lookup  

|     |     |
| --- | --- |
| **Returns a list of users who are muted by the specified user ID** | `[GET /2/users/:id/muting](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/get-users-muting)` |

### Manage mutes  

|     |     |
| --- | --- |
| **Allows a user ID to mute another user** | `[POST /2/users/:id/muting](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/post-users-user_id-muting)` |
| **Allows a user ID to unmute another user** | `[DELETE /2/users/:source_user_id/muting/:target_user_id](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/delete-users-user_id-muting)` |