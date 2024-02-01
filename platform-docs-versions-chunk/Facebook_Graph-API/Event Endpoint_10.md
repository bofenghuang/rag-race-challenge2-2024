platform: Facebook
topic: Graph-API
subtopic: Event Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Event Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/event/live_videos/


### Parameters

| Parameter | Description |
| --- | --- |
| `content_tags`<br><br>list<numeric string> | Tags that describe the contents of the video. Use search endpoint with `type=adinterest` to get possible IDs.<br><br>                                    Example:<br>                                    ~~~~<br>                                    /search?type=adinterest&q=couscous<br>                                    ~~~~ |
| `description`<br><br>UTF-8 string | The description of the live video.<br><br>Supports Emoji |
| `enable_backup_ingest`<br><br>boolean | Set this to true to enable a backup ingest url. stop\_on\_delete\_stream defaults to false when set |
| `encoding_settings`<br><br>string | Identifier of the encoding settings group the broadcaster is using for this stream. This parameter is currently only in use for live-360 broadcasts. The value to be passed to this parameter is the value of the `identifier` key of the encoding settings preset. Encoding presets can be found by querying the `/broadcaster_encoding_settings` Graph API endpoint (`GET` query). |
| `event_params`<br><br>Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event.<br><br>Example: { start\_time: 1641013200, cover: 'https://your.url/image.jpg', } |
| `fisheye_video_cropped`<br><br>boolean | Whether the single fisheye video is cropped or not |
| `front_z_rotation`<br><br>float | The front z rotation in degrees on the single fisheye video |
| `is_spherical`<br><br>boolean | Flag that denotes the broadcast is a 360 live broadcast. |
| `original_fov`<br><br>int64 | Original field of view of the camera |
| `privacy`<br><br>Privacy Parameter | Privacy for this live video. |
| `projection`<br><br>enum {EQUIRECTANGULAR, CUBEMAP, HALF\_EQUIRECTANGULAR} | Flag that denotes expected projection for 360 live streams. The default value is EQUIRECTANGULAR. |
| `published`<br><br>boolean | Set this to false to preview the stream before going live.<br><br>                                    Deprecated. Prefer setting the status instead. |
| `schedule_custom_profile_image`<br><br>image | Custom image that will appear in the scheduled live story and lobby. |
| `spatial_audio_format`<br><br>enum {ambiX\_4} | Denotes the format of the spatial audio stream. When unspecified audio is presumed to be mono or stereo. |
| `status`<br><br>enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the broadcast. A `LIVE_NOW` broadcast is currently live and visible to users. An `UNPUBLISHED` broadcast is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state. (Consider using the `SCHEDULED` states to create a planned, future broadcast.) |
| `stereoscopic_mode`<br><br>enum {MONO, LEFT\_RIGHT, TOP\_BOTTOM} | Set this parameter to the stereoscopic mode for this video. |
| `stop_on_delete_stream`<br><br>boolean | Set this to true if stream should be stopped when deleteStream RTMP command received. |
| `title`<br><br>UTF-8 string | The title of the live video. Maximum 254 characters.<br><br>Supports Emoji |