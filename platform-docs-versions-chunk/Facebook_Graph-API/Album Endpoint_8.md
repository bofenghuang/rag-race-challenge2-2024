platform: Facebook
topic: Graph-API
subtopic: Album Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Album Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/album/

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 100 | Invalid parameter |

## Creating

You can make a POST request to `albums` edge from the following paths:

* [`/{group_id}/albums`](https://developers.facebook.com/docs/graph-api/reference/group/albums/)

When posting to this edge, an [Album](https://developers.facebook.com/docs/graph-api/reference/album/) will be created.