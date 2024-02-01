platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/changelog

## April 24, 2018

* `/{ig-comment-id}` node:
    
    * Added a new `username` field.
    * For `GET` requests, the `user` field will not be included in responses unless the User making the request owns the Comment; instead, we will return `username` for all commenters. This also applies to queries on Comments made through other APIs, such as the Mentions API.
    
* `/{ig-media-id}` node:
    
    * Added a new `username` field.
    * For `GET` requests, the `owner` field will not be included in responses unless the User making the request owns the media object; instead, we will return `username` for all commenters. This also applies to queries on media objects made through other APIs, such as the Mentions API.
    

[](#)

## April 23, 2018

* **Insights API** — Insights will now include ad activity generated through the API, Facebook ads interfaces, and Instagram's Promote feature. This affects the following metrics:
    
    * `impressions`
    * `reach`
    

[](#)