platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/getting-started

## 5\. Get the Page's Instagram Business Account

Use the Page ID you captured to query the `GET /{page-id}?fields=instagram_business_account` endpoint:

curl \-i \-X GET \\
 "https://graph.facebook.com/`v19.0`/134895793791914?fields=instagram\_business\_account&access\_token={access-token}"

This should return the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) — an Instagram Business or Creator Account — that's connected to the Facebook Page.

{
  "instagram\_business\_account": {
    "id": "17841405822304914"  // Connected IG User ID
  },
  "id": "134895793791914"  // Facebook Page ID
}

Capture the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) ID.

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/57462471_316665542380805_102061440998834176_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=-0po3oJgQLYAX_bVgvd&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCUqjzi9SLILJ1KSjr9sElo26T32mS5QdExGMlWQOqVUw&oe=65D55DF9)

[](#)