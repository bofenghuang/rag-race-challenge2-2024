platform: Facebook
topic: Graph-API
subtopic: Live video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Live video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/live-video/blocked_users/

### Parameters

| Parameter | Description |
| --- | --- |
| `uid`<br><br>numeric string or integer | IDs of users who are blocked from the video broadcast |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [User](https://developers.facebook.com/docs/graph-api/reference/user/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 210 | User not visible |

## Creating

You can't perform this operation on this endpoint.

## Updating

You can't perform this operation on this endpoint.