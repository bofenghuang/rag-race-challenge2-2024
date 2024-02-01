platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs

### Channels

A `**channel**` resource contains information about a YouTube channel.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/channels#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/channels#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[list](https://developers.google.com/youtube/v3/docs/channels/list)` | `GET /channels` | Returns a collection of zero or more `**channel**` resources that match the request criteria. |
| `[update](https://developers.google.com/youtube/v3/docs/channels/update)` | `PUT /channels` | Updates a channel's metadata. Note that this method currently only supports updates to the `channel` resource's `brandingSettings` and `invideoPromotion` objects and their child properties. |