platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/businesses/

## Updating

You can't perform this operation on this endpoint.

## Deleting

You can dissociate a [Business](https://developers.facebook.com/docs/marketing-api/reference/business/) from a [User](https://developers.facebook.com/docs/graph-api/reference/user/) by making a DELETE request to [`/{user_id}/businesses`](https://developers.facebook.com/docs/graph-api/reference/user/businesses/).

### Parameters

| Parameter | Description |
| --- | --- |
| `business`<br><br>numeric string or integer | Business ID |

### Return Type

Struct {

`success`: bool,

}