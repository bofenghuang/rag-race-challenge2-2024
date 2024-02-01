platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/thumbnails/

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |

## Creating

You can make a POST request to `thumbnails` edge from the following paths:

* [`/{video_id}/thumbnails`](https://developers.facebook.com/docs/graph-api/reference/video/thumbnails/)

When posting to this edge, a [VideoThumbnail](https://developers.facebook.com/docs/graph-api/reference/video-thumbnail/) will be created.

### Limitations

* Maximum thumbnail file size 10MB.
* Thumbnails can only be created on [Videos](https://developers.facebook.com/docs/graph-api/reference/video/) that have been associated with a [Page](https://developers.facebook.com/docs/graph-api/reference/page/).
* We recommend that you use thumbnails with the same aspect ratio as the video.