platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/post-users-source_user_id-following

POST /2/users/:id/following

# POST /2/users/:id/following

Allows a user ID to follow another user.  
  
If the target user does not have public Tweets, this endpoint will send a follow request.  
  
The request succeeds with no action when the authenticated user sends a request to a user they're already following, or if they're sending a follower request to a user that does not have public Tweets.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdFollow&params=%28%27query%21%28%29%7Ebody%21%28%27target*2244994945%27%29%7Epath%21%28%21source*6253282%27%29%29*_user_id%21%27%01*_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Ffollowing&method=post) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/following`