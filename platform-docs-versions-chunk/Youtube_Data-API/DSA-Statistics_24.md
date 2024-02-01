platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs

### Watermarks

A `**watermark**` resource identifies an image that displays during playbacks of a specified channel's videos. You can also specify a target channel to which the image will link as well as timing details that determine when the watermark appears during video playbacks and the length of time it is visible.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/watermarks#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/watermarks#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[set](https://developers.google.com/youtube/v3/docs/watermarks/set)` | `POST /watermarks/set` | Uploads a watermark image to YouTube and sets it for a channel. |
| `[unset](https://developers.google.com/youtube/v3/docs/watermarks/unset)` | `POST /watermarks/unset` | Deletes a channel's watermark image. |