platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/button_auto_detection_device_selection/

### Parameters

| Parameter | Description |
| --- | --- |
| `device_id`<br><br>string | Device id of the given app. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of ButtonAutoDetectionDeviceSelection nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 43003 | App auto button detection is disabled. |
| 100 | Invalid parameter |
| 200 | Permissions error |

## Creating

You can't perform this operation on this endpoint.

## Updating

You can't perform this operation on this endpoint.