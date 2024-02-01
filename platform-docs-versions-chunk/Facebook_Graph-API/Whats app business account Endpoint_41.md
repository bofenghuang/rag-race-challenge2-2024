platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/product_catalogs/

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ProductCatalog](https://developers.facebook.com/docs/marketing-api/reference/product-catalog/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

## Creating

You can make a POST request to `product_catalogs` edge from the following paths:

* [`/{whats_app_business_account_id}/product_catalogs`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/product_catalogs/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `catalog_id`<br><br>Product Catalog ID | catalog\_id<br><br>Required |