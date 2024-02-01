platform: Facebook
topic: Graph-API
subtopic: Commerce merchant settings Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Commerce merchant settings Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/commerce_payouts/

### Parameters

| Parameter | Description |
| --- | --- |
| `end_time`<br><br>datetime/timestamp | The end time until which the payouts should be fetched |
| `start_time`<br><br>datetime/timestamp | The start time from which the payouts should be fetched |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of CommercePayout nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

## Creating

You can't perform this operation on this endpoint.

## Updating

You can't perform this operation on this endpoint.