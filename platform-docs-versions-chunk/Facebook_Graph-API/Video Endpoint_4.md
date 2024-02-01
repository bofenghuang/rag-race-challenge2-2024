platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/captions/

### Limitations

The file size limit for video captions is 200K.  
  

You can update a [Video](https://developers.facebook.com/docs/graph-api/reference/video/) by making a POST request to [`/{video_id}/captions`](https://developers.facebook.com/docs/graph-api/reference/video/captions/).

### Parameters

| Parameter | Description |
| --- | --- |
| `captions_file`<br><br>file | Caption file in SRT (SubRip Text) format. File name must be in the format filename.locale.srt |
| `default_locale`<br><br>string | Specify which locale should be used as the default for the video. Can be set to 'none' |
| `locales_to_delete`<br><br>list<string> | Default value: `Vector`<br><br>locales of caption to delete |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}