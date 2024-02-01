platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### Subscriptions

A `**subscription**` resource contains information about a YouTube user subscription. A subscription notifies a user when new videos are added to a channel or when another user takes one of several actions on YouTube, such as uploading a video, rating a video, or commenting on a video.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/subscriptions#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/subscriptions#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[delete](https://developers.google.com/youtube/v3/docs/subscriptions/delete)` | `DELETE /subscriptions` | Deletes a subscription. |
| `[insert](https://developers.google.com/youtube/v3/docs/subscriptions/insert)` | `POST /subscriptions` | Adds a subscription for the authenticated user's channel. |
| `[list](https://developers.google.com/youtube/v3/docs/subscriptions/list)` | `GET /subscriptions` | Returns subscription resources that match the API request criteria. |