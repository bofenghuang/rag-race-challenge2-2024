platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/payment_currencies/

# Application Payment Currencies

## Reading

You can't perform this operation on this endpoint.

## Creating

You can make a POST request to `payment_currencies` edge from the following paths:

* [`/{application_id}/payment_currencies`](https://developers.facebook.com/docs/graph-api/reference/application/payment_currencies/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `currency_url`<br><br>URL | SELF\_EXPLANATORY<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

## Updating

You can't perform this operation on this endpoint.