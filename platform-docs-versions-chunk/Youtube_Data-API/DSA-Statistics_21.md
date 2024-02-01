platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### VideoAbuseReportReasons

A `**videoAbuseReportReason**` resource contains information about a reason that a video would be flagged for containing abusive content. When your application calls the `[videos.reportAbuse](https://developers.google.com/youtube/v3/docs/videos/reportAbuse)` method to report an abusive video, the request uses the information from a `videoAbuseReportReason` resource to identify the reason that the video is being reported.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[list](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list)` | `GET /videoAbuseReportReasons` | Retrieve a list of reasons that can be used to report abusive videos. |