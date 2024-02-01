platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/videos/


### Parameters

| Parameter | Description |
| --- | --- |
| `audio_story_wave_animation_handle`<br><br>string | Everstore handle of wave animation used to burn audio story video |
| `content_category`[](#)<br><br>enum {BEAUTY\_FASHION, BUSINESS, CARS\_TRUCKS, COMEDY, CUTE\_ANIMALS, ENTERTAINMENT, FAMILY, FOOD\_HEALTH, HOME, LIFESTYLE, MUSIC, NEWS, POLITICS, SCIENCE, SPORTS, TECHNOLOGY, VIDEO\_GAMING, OTHER} | Content category of this video. |
| `description`<br><br>UTF-8 string | The text describing a post that may be shown in a story about it.<br>                                                                  It may include rich text information, such as entities and emojis.<br>    <br><br>Supports Emoji |
| `direct_share_status`<br><br>int64 | The status to allow sponsor directly boost the post. |
| `embeddable`[](#)<br><br>boolean | Whether the video is embeddable. |
| `end_offset`[](#)<br><br>int64 | end\_offset |
| `file_size`[](#)<br><br>int64 | The size of the entire video file in bytes. |
| `file_url`<br><br>string | Accessible URL of a video file. Cannot be used with `upload_phase`. |
| `fisheye_video_cropped`<br><br>boolean | Whether the single fisheye video is cropped or not |
| `fov`<br><br>int64 | 360 video only: Vertical field of view |
| `front_z_rotation`<br><br>float | The front z rotation in degrees on the single fisheye video |
| `guide`<br><br>list<list<int64>> | 360 video only: Guide keyframes data. An array of keyframes, each of which is an array of 3 or 4 elements in the following order: \[video timestamp (seconds), pitch (degrees, -90 ~ 90), yaw (degrees, -180 ~ 180), field of view (degrees, 40 ~ 90, optional)\], ordered by video timestamp in strictly ascending order. |
| `guide_enabled`<br><br>boolean | 360 video only: Whether Guide is active. |
| `initial_heading`<br><br>int64 | 360 video only: Horizontal camera perspective to display when the video begins. |
| `initial_pitch`<br><br>int64 | 360 video only: Vertical camera perspective to display when the video begins. |
| `is_voice_clip`[](#)<br><br>boolean | is\_voice\_clip, used to indicate that if a video is used as audio record |
| `no_story`<br><br>boolean | Default value: `false`<br><br>If set to `true`, this will suppress feed and timeline story. |
| `original_fov`<br><br>int64 | Original field of view of the source camera |
| `original_projection_type`[](#)<br><br>enum {equirectangular, cubemap, half\_equirectangular} | 360 video only: The original projection type of the 360 video being uploaded. |
| `posting_to_redspace`[](#)<br><br>enum {enabled, disabled} | Whether the post should appear in RedSpace. |
| `privacy`<br><br>Privacy Parameter | Determines the [privacy settings](https://developers.facebook.com/docs/graph-api/common-scenarios#privacy-param) of the video. If not supplied, this defaults to the privacy level granted to the app in the Login Dialog. This field cannot be used to set a more open privacy setting than the one granted. |
| `prompt_id`[](#)<br><br>string | The prompt id in prompts or purple rain that generated this post |
| `prompt_tracking_string`[](#)<br><br>string | The prompt tracking string associated with this video post |
| `react_mode_metadata`<br><br>JSON-encoded string | This metadata is required for clip reacts feature |
| `referenced_sticker_id`<br><br>numeric string or integer | Sticker id of the sticker in the post |
| `replace_video_id`[](#)<br><br>numeric string or integer | The video id your uploaded video about to replace |
| `slideshow_spec`<br><br>JSON object | Specification of a list of images that are used to generate video. |
| `images_urls`<br><br>list<URL> | A 3-7 element array of the URLs of the images. Required.<br><br>Required |
| `duration_ms`<br><br>integer | The duration in milliseconds of each image. Default value is 1000. |
| `transition_ms`<br><br>integer | The duration in milliseconds of the crossfade transition between images. Default value is 1000. |
| `reordering_opt_in`<br><br>boolean | Default value: `false` |
| `music_variations_opt_in`<br><br>boolean | Default value: `false` |
| `source`<br><br>string | The video, [encoded as form data](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml401%2Finteract%2Fforms.html%23h-17.13.4.2&h=AT0vv53hpFwwE4DWfQ7v4zWEnkPaAw9wQtEEHpIGkaRw1PqgCbZP_upYlDdSaed-ERjuosbVA8Rkzf4u-filebI7ui0JrfacpDxLZgkoZ02VyLJLdCKTXYJwbPLbZRkLGLw6udLHv9DfSPli). This field is required. |
| `spherical`<br><br>boolean | Default value: `false`<br><br>Set if the video was recorded in 360 format. |
| `sponsor_id`<br><br>numeric string or integer | Facebook Page id that is tagged as sponsor in the video post |
| `start_offset`[](#)<br><br>int64 | Start byte position of the file chunk. |
| `swap_mode`[](#)<br><br>enum {replace} | Type of replacing video request |
| `title`<br><br>UTF-8 string | The title of the video<br><br>Supports Emoji |
| `transcode_setting_properties`[](#)<br><br>string | Properties used in computing transcode settings for the video |
| `unpublished_content_type`<br><br>enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | Type of unpublished content, such as scheduled, draft or ads\_post. |
| `upload_phase`[](#)<br><br>enum {start, transfer, finish, cancel} | Type of chunked upload request. |
| `upload_session_id`[](#)<br><br>numeric string or integer | ID of the chunked upload session. |
| `video_file_chunk`[](#)<br><br>string | The video file chunk, [encoded as form data](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml401%2Finteract%2Fforms.html%23h-17.13.4.2&h=AT3DwlctRuOQHgWEljy9EG0kOD5a2XCQckpttNSGrTItUrzvm0Y0fZbbaqj6w5r6ndxBRRpv5ENQ-oWWOEUAfvQ5-bhwdSzLv8Nv6oa5lb7pooyOG0640eReWOrhKHa5TyAUYJf2vQrFnWEO). This field is required during `transfer` upload phase. |
| `video_id_original`[](#)<br><br>string | video\_id\_original |