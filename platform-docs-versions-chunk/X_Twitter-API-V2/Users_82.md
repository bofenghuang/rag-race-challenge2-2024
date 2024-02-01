platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/delete-users-source_id-following

DELETE /2/users/:source\_user\_id/following/:target\_user\_id

# DELETE /2/users/:source\_user\_id/following/:target\_user\_id

Allows a user ID to unfollow another user.  
  
The request succeeds with no action when the authenticated user sends a request to a user they're not following or have already unfollowed.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdUnfollow&params=%28%27query%21%28%29%7Ebody%21%28%29%7Epath%21%28%21source*6253282%27%2C%21target*2244994945%27%29%29*_user_id%21%27%01*_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bsource_user_id%7D%2Ffollowing%2F%7Btarget_user_id%7D&method=delete) 

### Endpoint URL

`https://api.twitter.com/2/users/:source_user_id/following/:target_user_id`