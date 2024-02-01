platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media

# IG Media

Represents an Instagram album, photo, or video (uploaded video, live video, video created with the Instagram TV app, reel, or story).

## Creating

This operation is not supported.

## Reading

**`GET /{ig-media-id}`**

Gets [fields](#fields) and [edges](#edges) on IG media.

### Limitations

* Fields that return aggregated values don't include ads-driven data. For example, `comments_count` counts comments on a photo, but not comments on ads that contain that photo.
* Captions don't include the `@` symbol unless the app user is also able to perform Admin-equivalent [tasks](https://developers.facebook.com/docs/pages/overview#tasks) on the app.
* Some fields, such as `permalink`, cannot be used on photos within albums (children).
* Instagram TV media must be shared to Instagram at the time of publish (**Post a Preview** or **Share Preview to Feed** enabled) in order to be accessible via the API.
* Live video IG Media can only be read while they are being broadcast.