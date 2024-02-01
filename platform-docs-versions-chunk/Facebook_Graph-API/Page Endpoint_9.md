platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/

### Error Codes

| Error | Description |
| --- | --- |
| 551 | This person isn't available right now. |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 504 | Invalid reply thread id |

You can make a POST request to `personas` edge from the following paths:

* [`/{page_id}/personas`](https://developers.facebook.com/docs/graph-api/reference/page/personas/)

When posting to this edge, a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `name`<br><br>string | Name of a Persona<br><br>Required |
| `profile_picture_url`<br><br>URI | Profile picture of a Persona<br><br>Required |

### Return Type

Struct {

`id`: numeric string,

}