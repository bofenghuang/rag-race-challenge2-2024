platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/aem_conversion_filter/

### Parameters

| Parameter | Description |
| --- | --- |
| `catalog_id`<br><br>string | catalog\_id. Check the product\_ids are in this catalog. |
| `fb_content_ids`<br><br>string | product\_set\_ids, or fb\_content\_ids. Check these are in catalog\_id |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of AEMConversionFilter nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

## Creating

You can't perform this operation on this endpoint.

## Updating

You can't perform this operation on this endpoint.