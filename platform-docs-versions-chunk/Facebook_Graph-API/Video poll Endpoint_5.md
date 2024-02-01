platform: Facebook
topic: Graph-API
subtopic: Video poll Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video poll Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video-poll/

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

## Updating

You can update a [VideoPoll](https://developers.facebook.com/docs/graph-api/reference/video-poll/) by making a POST request to [`/{video_poll_id}`](https://developers.facebook.com/docs/graph-api/reference/video-poll/).

### Parameters

| Parameter | Description |
| --- | --- |
| `action`<br><br>enum {ATTACH\_TO\_VIDEO, CLOSE, SHOW\_VOTING, SHOW\_RESULTS, DELETE\_POLL} | Change state for the poll<br><br>Required |
| `show_results`<br><br>boolean | True if the viewer sees results after voting, false if they do not |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |