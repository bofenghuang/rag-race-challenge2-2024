platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/thumbnails/

### Examples

curl -X POST "https://graph.facebook.com/**_`v19.0`_**/**_video-id_**/thumbnails
   ?access\_token=**_page\_access\_token_**
   &is\_preferred=**_true_**
   &source=@**_ThumbnailSample1.jpg_**"

On success your app receives a list of VideoThumbnail objects for the video.

{
  "success": **_true_**
}

### Parameters

| Parameter | Description |
| --- | --- |
| `is_preferred`<br><br>boolean | Default value: `false`<br><br>Set to `true` if this thumbnail is the preferred thumbnail to be shown for this video |
| `source`<br><br>image | The source for the thumbnail, an image file<br><br>Required |

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

## Updating

You can't perform this operation on this endpoint.