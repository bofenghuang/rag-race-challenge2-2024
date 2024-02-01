platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/content-publishing


## Single Media Posts

Publishing single image, video, story or reel is a two-step process:

1. Use the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint to create a container from an image or video hosted on your public server.
2. Use the [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) endpoint to publish the container.

Step 1 of 2: Create Container

Let's say you have an image at...

https://www.example.com/images/bronz-fonz.jpg

... that you want to publish with the hashtag "#BronzFonz" as its caption. Send a request to the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint:

#### Sample Request

POST https://graph.facebook.com/`v19.0`/17841400008460056/media
  ?image\_url\=https://www.example.com/images/bronz-fonz.jpg
  &caption\=#BronzFonz

This returns a container ID for the image.

#### Sample Response

{
  "id": "17889455560051444"  // IG Container ID
}

Step 2 of 2: Publish Container

Use the `POST /{ig-user-id}/media_publish` endpoint to publish the container ID returned in the previous step.

#### Sample Request

POST https://graph.facebook.com/`v19.0`/17841400008460056/media\_publish
  ?creation\_id=17889455560051444

#### Sample Response

{
  "id": "17920238422030506" // IG Media ID
}

[](#)