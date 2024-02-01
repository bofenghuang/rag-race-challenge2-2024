platform: Facebook
topic: Graph-API
subtopic: Live video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Live video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/live-video/polls/

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [VideoPoll](https://developers.facebook.com/docs/graph-api/reference/video-poll/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

## Creating

You can make a POST request to `polls` edge from the following paths:

* [`/{live_video_id}/polls`](https://developers.facebook.com/docs/graph-api/reference/live-video/polls/)

When posting to this edge, a [VideoPoll](https://developers.facebook.com/docs/graph-api/reference/video-poll/) will be created.