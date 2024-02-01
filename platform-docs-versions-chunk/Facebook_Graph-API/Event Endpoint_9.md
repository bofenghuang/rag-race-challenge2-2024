platform: Facebook
topic: Graph-API
subtopic: Event Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Event Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/event/live_videos/

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of Null nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

## Creating

You can make a POST request to `live_videos` edge from the following paths:

* [`/{event_id}/live_videos`](https://developers.facebook.com/docs/graph-api/reference/event/live_videos/)

When posting to this edge, a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) will be created.