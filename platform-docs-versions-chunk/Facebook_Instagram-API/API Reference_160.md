platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media

### Sample Request

POST graph.facebook.com/17841400008460056/media
  ?image\_url=https//www.example.com/images/bronzed-fonzes.jpg
  &caption=#BronzedFonzes!
  &collaborators= \[‘username1’,’username2’\]
  &user\_tags=\[
    {
      username:'kevinhart4real',
      x: 0.5,
      y: 0.8
    },
    {
      username:'therock',
      x: 0.3,
      y: 0.2
    }
  \]

### Sample Response

{
  "id": "17889455560051444"
}

## Reading

**`GET /{ig-user-id}/media`**

Get all [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

### Limitations

* Returns a maximum of 10K of the most recently created media.
* Story IG Media not supported, use the [`GET /{ig-user-id}/stories`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/stories) endpoint instead.