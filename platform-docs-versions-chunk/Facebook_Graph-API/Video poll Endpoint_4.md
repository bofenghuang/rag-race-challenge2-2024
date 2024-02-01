platform: Facebook
topic: Graph-API
subtopic: Video poll Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video poll Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video-poll/

## Creating

You can make a POST request to `polls` edge from the following paths:

* [`/{live_video_id}/polls`](https://developers.facebook.com/docs/graph-api/reference/live-video/polls/)

When posting to this edge, a [VideoPoll](https://developers.facebook.com/docs/graph-api/reference/video-poll/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `correct_option`<br><br>int64 | Number of the correct option (in order, starting from 1) |
| `options`<br><br>array<string> | Text options for users to select in order<br><br>Required |
| `question`<br><br>string | Question text<br><br>Required |
| `show_results`<br><br>boolean | True to show the results after voting, otherwise false |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`option_ids`: List \[

numeric string

\],

}