platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/videos/

### Parameters

| Parameter | Description |
| --- | --- |
| `type`<br><br>enum {TAGGED, UPLOADED} | Default value: `"TAGGED"`<br><br>Allows you to query which type of videos to return |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [Video](https://developers.facebook.com/docs/graph-api/reference/video/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |

## Creating

You can make a POST request to `videos` edge from the following paths:

* [`/{user_id}/videos`](https://developers.facebook.com/docs/graph-api/reference/user/videos/)

When posting to this edge, a [Video](https://developers.facebook.com/docs/graph-api/reference/video/) will be created.