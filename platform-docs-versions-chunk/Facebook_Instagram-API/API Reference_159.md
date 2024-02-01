platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media

### Response

A JSON-formatted object containing an [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) ID which you can use to [publish](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish) the container.

Video uploads are asynchronous, so receiving a container ID does not guarantee that the upload was successful. To verify that a video has been uploaded, request the [`status_code`](https://developers.facebook.com/docs/instagram-api/reference/ig-container#fields) field on the IG Container. If its value is `FINISHED`, the video was uploaded successfully.

{
  "id":"{ig-container-id}"
}