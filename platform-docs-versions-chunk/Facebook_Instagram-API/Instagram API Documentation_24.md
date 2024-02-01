platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/getting-started


## 4\. Get the User's Pages

Query the `GET /me/accounts` endpoint (this translates to `GET /{user-id}/accounts`, which perform a `GET` on the Facebook [User](https://developers.facebook.com/docs/graph-api/reference/user) node, based on your access token).

curl \-i \-X GET \\
 "https://graph.facebook.com/`v19.0`/me/accounts?access\_token={access-token}"

This should return a collection of Facebook Pages that the current Facebook User can perform the `MANAGE`, `CREATE_CONTENT`, `MODERATE`, or `ADVERTISE` tasks on:

{
  "data": \[
    {
      "access\_token": "EAAJjmJ...",
      "category": "App Page",
      "category\_list": \[
        {
          "id": "2301",
          "name": "App Page"
        }
      \],
      "name": "Metricsaurus",
      "id": "134895793791914",  // capture the Page ID
      "tasks": \[
        "ANALYZE",
        "ADVERTISE",
        "MODERATE",
        "CREATE\_CONTENT",
        "MANAGE"
      \]
    }
  \]
}

Capture the ID of the Facebook Page that's connected to the Instagram account that you want to query. Keep in mind that your app users may be able to perform tasks on multiple pages, so you eventually will have to introduce logic that can determine the correct Page ID to capture (or devise a UI where your app users can identify the correct Page for you).

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/57437240_2085096038272793_3947769475595501568_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=syxNAwtOUmgAX8YeajH&_nc_ht=scontent-cdg4-3.xx&oh=00_AfAR7-LLxyEG-7gY7TKri-Mp85WPsGUvL1oZMpJH6JiATg&oe=65D578C6)

[](#)