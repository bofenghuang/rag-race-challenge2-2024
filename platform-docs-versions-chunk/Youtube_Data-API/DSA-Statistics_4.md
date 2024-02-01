platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### Activities

An `**activity**` resource contains information about an action that a particular channel, or user, has taken on YouTube. The actions reported in activity feeds include rating a video, sharing a video, marking a video as a favorite, uploading a video, and so forth. Each `activity` resource identifies the type of action, the channel associated with the action, and the resource(s) associated with the action, such as the video that was rated or uploaded.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/activities#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/activities#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[list](https://developers.google.com/youtube/v3/docs/activities/list)` | `GET /activities` | Returns a list of channel activity events that match the request criteria. For example, you can retrieve events associated with a particular channel or with the user's own channel. |
| `[insert](https://developers.google.com/youtube/v3/docs/activities/insert)` | `POST /activities` | **Note:** This method has been deprecated and is no longer supported. |