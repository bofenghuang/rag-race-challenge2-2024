platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs

### GuideCategories

A `**guideCategory**` resource identifies a category that YouTube algorithmically assigns based on a channel's content or other indicators, such as the channel's popularity. The list is similar to [video categories](https://developers.google.com/youtube/v3/docs/videoCategories), with the difference being that a video's uploader can assign a video category but only YouTube can assign a channel category.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/guideCategories#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/guideCategories#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[list](https://developers.google.com/youtube/v3/docs/guideCategories/list)` | `GET /guideCategories` | Returns a list of categories that can be associated with YouTube channels. |