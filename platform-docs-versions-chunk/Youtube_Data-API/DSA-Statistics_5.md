platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### Captions

A `**caption**` resource represents a YouTube caption track. A caption track is associated with exactly one YouTube video.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/captions#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/captions#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[delete](https://developers.google.com/youtube/v3/docs/captions/delete)` | `DELETE /captions` | Deletes the specified caption track. |
| `[download](https://developers.google.com/youtube/v3/docs/captions/download)` | `GET /captions/id` | Downloads a caption track. The caption track is returned in its original format unless the request specifies a value for the `tfmt` parameter and in its original language unless the request specifies a value for the `tlang` parameter. |
| `[insert](https://developers.google.com/youtube/v3/docs/captions/insert)` | `POST /captions` | Uploads a caption track. |
| `[list](https://developers.google.com/youtube/v3/docs/captions/list)` | `GET /captions` | Returns a list of caption tracks that are associated with a specified video. Note that the API response does not contain the actual captions and that the `[captions.download](https://developers.google.com/youtube/v3/docs/captions/download)` method provides the ability to retrieve a caption track. |
| `[update](https://developers.google.com/youtube/v3/docs/captions/update)` | `PUT /captions` | Updates a caption track. When updating a caption track, you can change the track's [draft status](https://developers.google.com/youtube/v3/docs/captions#snippet.isDraft), upload a new caption file for the track, or both. |