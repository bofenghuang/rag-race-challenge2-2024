platform: Facebook
topic: Graph-API
subtopic: Page post Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page post Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page-post/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 210 | User not visible |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

## Deleting

Only select developers can perform this operation using the API. You can use the [Business Manager](#) to delete posts.

You can delete a [PagePost](https://developers.facebook.com/docs/graph-api/reference/page-post/) by making a DELETE request to [`/{page_post_id}`](https://developers.facebook.com/docs/graph-api/reference/page-post/).