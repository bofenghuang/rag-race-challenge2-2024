platform: Facebook
topic: Graph-API
subtopic: Commerce merchant settings Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Commerce merchant settings Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/returns/

### Parameters

| Parameter | Description |
| --- | --- |
| `end_time_created`<br><br>datetime/timestamp | Default value: `1706766107`<br><br>Limit to returns created before a certain time |
| `merchant_return_id`<br><br>string | Filter to find returns with matching merchant\_return\_id, which was provided when approving/disapproving a return. |
| `start_time_created`<br><br>datetime/timestamp | Default value: `0`<br><br>Limit to returns created after a certain time |
| `statuses`<br><br>array<enum {APPROVED, DISAPPROVED, MERCHANT\_MARKED\_COMPLETED, REFUNDED, REQUESTED}> | Default value: `[]`<br><br>Filter by return status |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of CommerceReturn nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).