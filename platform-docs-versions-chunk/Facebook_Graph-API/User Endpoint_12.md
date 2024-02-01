platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`audience_id`: numeric string,

`session_id`: numeric string,

`num_received`: int32,

`num_invalid_entries`: int32,

`invalid_entry_samples`: Map {

string: string

},

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 2650 | Failed to update the custom audience |
| 190 | Invalid OAuth 2.0 Access Token |
| 105 | The number of parameters exceeded the maximum for this operation |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

## Deleting

Delete a test user

You can delete a [User](https://developers.facebook.com/docs/graph-api/reference/user/) by making a DELETE request to [`/{user_id}`](https://developers.facebook.com/docs/graph-api/reference/user/).

### Parameters

This endpoint doesn't have any parameters.