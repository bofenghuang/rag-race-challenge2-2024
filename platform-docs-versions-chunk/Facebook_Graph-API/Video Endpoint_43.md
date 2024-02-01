platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/thumbnails/

### Examples

curl -X GET "https://graph.facebook.com/**_`v19.0`_**/**_video-id_**/thumbnails?access\_token=**_page\_access\_token_**"

On success your app receives a list of VideoThumbnail objects for the video.

{
"id": "**_video-id-1_**",
"height": **_1280_**,
"scale": 1,
"uri": "**_url-for-video-1_**",
"width": **_720_**,
"is\_preferred": **_false_**
},
{
"id": "**_video-id-2_**",
"height": **_1280_**,
"scale": 1,
"uri": "**_url-for-video-2_**",
"width": **_720_**,
"is\_preferred": **_false_**
},
...

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [VideoThumbnail](https://developers.facebook.com/docs/graph-api/reference/video-thumbnail/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).