platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/comments/

### Parameters

| Parameter | Description |
| --- | --- |
| `attachment_id`<br><br>numeric string or integer | ID for a photo attachment to associate with this |
| `attachment_share_url`<br><br>URL | Link to set the comment attachment to. Does not include the url in the message |
| `attachment_url`<br><br>URL | Link to set the comment attachment to |
| `is_offline`<br><br>boolean | Whether the comment was originally made while offline |
| `message`<br><br>UTF-8 string | Same as the text param<br><br>Supports Emoji |
| `text`<br><br>UTF-8 string | The text of the comment that allows emoji<br><br>Supports Emoji |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: token with structure: Comment ID,

}