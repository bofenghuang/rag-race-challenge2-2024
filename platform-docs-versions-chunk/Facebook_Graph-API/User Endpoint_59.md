platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/assigned_product_catalogs/

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [ProductCatalog](https://developers.facebook.com/docs/marketing-api/reference/product-catalog/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `access_type`<br><br>string | Checks if business has owner or agency access on the asset |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>int32 | Total number of objects on this edge<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |