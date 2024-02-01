platform: Facebook
topic: Graph-API
subtopic: Album Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Album Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/album/picture/

### Parameters

| Parameter | Description |
| --- | --- |
| `redirect`<br><br>boolean | Default value: `true`<br><br>By default the picture edge will return a picture instead of a JSON response. If you want the picture edge to return JSON that describes the image set `redirect=0` when you make the request. |
| `type`<br><br>enum{thumbnail, small, album} | Default value: `album`<br><br>The size of this picture. It can be one of the following values: thumbnail, small, album. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ProfilePictureSource](https://developers.facebook.com/docs/graph-api/reference/profile-picture-source/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |