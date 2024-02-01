platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/getting-started


## 6\. Get the Instagram Business Account's Media Objects

Use the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) ID you captured to query the `GET /{ig-user-id}/media` endpoint:

curl \-i \-X GET \\
 "https://graph.facebook.com/`v19.0`/17841405822304914/media?access\_token={access-token}"

This should return the IDs of all the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user):

{
  "data": \[
    {
      "id": "17918195224117851"
    },
    {
      "id": "17895695668004550"
    },
    {
      "id": "17899305451014820"
    },
    {
      "id": "17896450804038745"
    },
    {
      "id": "17881042411086627"
    },
    {
      "id": "17869102915168123"
    }
  \],
  "paging": {
    "cursors": {
      "before": "QVFIUkdGRXA2eHNNTUs4T1ZAXNGFxQTAtd3U4QjBLd1B2NXRMM1NkcnhqRFdBcEUzSDVJZATFoLWtXMWZAGU2VrRTk2RHVtTVlDckI2NjN0UERFa2JrUk4yMW13",
      "after": "QVFIUmlwbnFsM3N2cV9lZAFdCa0hDeV9qMVliT0VuMmJyNENxZA180c0t6VjFQVEJaTE9XV085aU92OUFLNFB6Szd2amo5aV9rTlVBcnNlWmEtMzYxcE1HSFR3"
    }
  }
}

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/57261700_588761411631102_2933352179429277696_n.png?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=nHGXEwU5TDoAX8B2Mf3&_nc_ht=scontent-cdg4-1.xx&oh=00_AfBWAWnpCmu9Qt3sak82sUiRRXOTcCsRdHYTxjz4yIiPSg&oe=65D555FD)

If you are able to perform this final query successfully, you should be able to perform queries using any of the Instagram Graph API endpoints — just refer to our various guides and references to learn what each endpoint can do and what permissions they require.

[](#)