platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/picture/

### Parameters

| Parameter | Description |
| --- | --- |
| `height`<br><br>integer | The height of this picture in pixels. |
| `redirect`<br><br>boolean | Default value: `true`<br><br>By default the picture edge will return a picture instead of a JSON response. If you want the picture edge to return JSON that describes the image set `redirect=0` when you make the request. |
| `type`<br><br>enum{small, normal, album, large, square} | The size of this picture. It can be one of the following values: small, normal, large, square. |
| `width`<br><br>integer | The width of this picture in pixels. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A single [ProfilePictureSource](https://developers.facebook.com/docs/graph-api/reference/profile-picture-source/) node.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).