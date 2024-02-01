platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### Videos

A `**video**` resource represents a YouTube video.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/videos#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/videos#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[insert](https://developers.google.com/youtube/v3/docs/videos/insert)` | `POST /videos` | Uploads a video to YouTube and optionally sets the video's metadata. |
| `[list](https://developers.google.com/youtube/v3/docs/videos/list)` | `GET /videos` | Returns a list of videos that match the API request parameters. |
| `[delete](https://developers.google.com/youtube/v3/docs/videos/delete)` | `DELETE /videos` | Deletes a YouTube video. |
| `[update](https://developers.google.com/youtube/v3/docs/videos/update)` | `PUT /videos` | Updates a video's metadata. |
| `[rate](https://developers.google.com/youtube/v3/docs/videos/rate)` | `POST /videos/rate` | Add a like or dislike rating to a video or remove a rating from a video. |
| `[getRating](https://developers.google.com/youtube/v3/docs/videos/getRating)` | `GET /videos/getRating` | Retrieves the ratings that the authorized user gave to a list of specified videos. |
| `[reportAbuse](https://developers.google.com/youtube/v3/docs/videos/reportAbuse)` | `POST /videos/reportAbuse` | Report a video for containing abusive content. |