platform: Facebook
topic: Graph-API
subtopic: Commerce merchant settings Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Commerce merchant settings Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/commerce_orders/

### Parameters

| Parameter | Description |
| --- | --- |
| `filters`<br><br>array<enum {HAS\_FULFILLMENTS, HAS\_CANCELLATIONS, HAS\_REFUNDS, NO\_SHIPMENTS, NO\_CANCELLATIONS, NO\_REFUNDS}> | Various filters to sort through the orders |
| `state`<br><br>array<enum {FB\_PROCESSING, CREATED, IN\_PROGRESS, COMPLETED}> | The state of the order (added support for multi-item in v3.3+) |
| `updated_after`<br><br>datetime/timestamp | Updated after time |
| `updated_before`<br><br>datetime/timestamp | Updated before time |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [CommerceOrder](https://developers.facebook.com/docs/graph-api/reference/commerce-order/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |