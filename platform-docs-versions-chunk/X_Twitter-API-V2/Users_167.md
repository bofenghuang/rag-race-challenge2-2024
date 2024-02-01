platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/delete-users-user_id-muting

DELETE /2/users/:source\_user\_id/muting/:target\_user\_id

# DELETE /2/users/:source\_user\_id/muting/:target\_user\_id

Allows an authenticated user ID to unmute the target user.  
  
The request succeeds with no action when the user sends a request to a user they're not muting or have already unmuted.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdUnmute&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bsource_user_id%7D%2Fmuting%2F%7Btarget_user_id%7D&method=delete) 

### Endpoint URL

`https://api.twitter.com/2/users/:source_user_id/muting/:target_user_id`