platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/accounts/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`access_token`: string,

`login_url`: string,

`email`: string,

`password`: string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 2900 | Too many test accounts |

## Updating

You can't perform this operation on this endpoint.

## Deleting

You can dissociate a [TestAccount](https://developers.facebook.com/docs/graph-api/reference/test-account/) from an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) by making a DELETE request to [`/{application_id}/accounts`](https://developers.facebook.com/docs/graph-api/reference/application/accounts/).