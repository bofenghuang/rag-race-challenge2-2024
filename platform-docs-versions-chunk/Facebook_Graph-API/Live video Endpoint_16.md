platform: Facebook
topic: Graph-API
subtopic: Live video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Live video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/live-video/


### Parameters

| Parameter | Description |
| --- | --- |
| `allow_bm_crossposting`<br><br>boolean | If set to true, makes this live video available for crossposting by Pages in your Business Manager. |
| `content_tags`<br><br>list<numeric string> | Tags that describe the contents of the video. Use search endpoint with `type=adinterest` to get possible IDs. For example, `/search?type=adinterest&q=couscous`. |
| `cross_share_to_group_ids`<br><br>list<numeric string> | List of Groups by ID where the broadcast will be shared. The broadcast owner will require publishing permission to the groups in order to share. |
| `crossposting_actions`<br><br>array<JSON object> | List of desired changes to crossposting for this broadcast. Each change must provide a `page_id` and `action`. Example:<br>    <br>    <br>                [<br>                  {page_id: 1234, action: 'enable_crossposting'},<br>                  {page_id: 4567, action: 'enable_crossposting_and_create_post'}<br>                ]<br>    <br>    <br>            Available action types:<br>    <br>    <br>            - `enable_crossposting`: Enables crossposting for this broadcast with the Page if it is not currently enabled. No change if crossposting is already enabled with the Page for this broadcast.<br>            - `disable_crossposting`: Disables crossposting for this broadcast with the Page if it is currently enabled. No change if crossposting is not already enabled with the Page for this broadcast.<br>            - `enable_crossposting_and_create_post`: Same as `enable_crossposting`, but will also create a post as the Page. The post will be created even if crossposting is already enabled for the Page. This option is subject to your [live crossposting relationships](https://www.facebook.com/help/publisher/1385580858214929) and will fail for Pages without the required permission.<br>    <br>            When used with a Live Online Event, this will apply to the event. |
| `page_id`<br><br>page ID | page\_id<br><br>Required |
| `action`<br><br>enum {ENABLE\_CROSSPOSTING, DISABLE\_CROSSPOSTING, ENABLE\_CROSSPOSTING\_AND\_CREATE\_POST} | action<br><br>Required |
| `custom_labels`<br><br>list<string> | Labels used to describe the video. Unlike content tags, custom labels are not published and only appear in insights data. |
| `description`<br><br>UTF-8 string | The description of live video<br><br>Supports Emoji |
| `direct_share_status`<br><br>int64 | The status to allow sponsor directly boost the post. |
| `disturbing`<br><br>boolean | If true, autoplay will be disabled and live video will have a graphic content warning overlay |
| `donate_button_charity_id`<br><br>int64 | Specifies the ID of the charity for which a donate button will be added to the live video. If zero is passed, will remove the donate button on the video. |
| `embeddable`<br><br>boolean | If true, live video will be embeddable |
| `end_live_video`<br><br>boolean | If true, the live video will be ended. Only valid if the live video is still running |
| `event_params`<br><br>Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event. Example: { start\_time: 1641013200, cover: 'https://your.url/image.jpg', } |
| `is_manual_mode`<br><br>boolean | Flag to indicate that the scheduled broadcast is switched to manual mode |
| `live_comment_moderation_setting`<br><br>list<enum {DEFAULT, FOLLOWER, SLOW, DISCUSSION, RESTRICTED, PROTECTED\_MODE, SUPPORTER, NO\_HYPERLINK, FOLLOWED, TAGGED}> | Set of comment moderation settings for the live video |
| `master_ingest_stream_id`<br><br>numeric string | Ingest stream to set to master and route viewers to. |
| `persistent_stream_key_status`<br><br>enum {ENABLE, DISABLE, REGENERATE} | Set the status of the persistent stream key for this live video |
| `place`<br><br>place tag | Location associated with the video, if any. |
| `planned_start_time`<br><br>datetime/timestamp | Planned start time for a scheduled live video |
| `privacy`<br><br>Privacy Parameter | The privacy setting of live video |
| `published`<br><br>boolean | Should the live video be published? Only valid if not yet published.<br><br>            Deprecated. Prefer setting the status instead. |
| `schedule_custom_profile_image`<br><br>image | Custom image that will appear in the scheduled live story and lobby. |
| `schedule_feed_background_image`<br><br>image | Custom background image that appears in the updated scheduled live story |
| `sponsor_id`<br><br>numeric string or integer | Facebook Page id that is tagged as sponsor in the video post |
| `sponsor_relationship`<br><br>int64 | Sponsor Relationship, such as Presented By or Paid PartnershipWith |
| `status`<br><br>enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the LiveVideo.<br><br>A `LIVE_NOW` LiveVideo is one that will be published to the intended destination (Timeline, Group, Page, etc) upon receiving valid video data, or one that is already published and actively streaming.<br><br>An `UNPUBLISHED` LiveVideo is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state.<br><br>A `SCHEDULED_UNPUBLISHED` LiveVideo is scheduled to go live at a future time.<br><br>A `SCHEDULED_LIVE` LiveVideo is one whose scheduled time has passed, yet the stream is not yet live. Either in the process of transitioning, or still waiting for a valid video stream.<br><br>(Consider using the `SCHEDULED` states to create a planned, future LiveVideo.) |
| `tags`<br><br>list<int> | Users tagged in the live video. |
| `targeting`<br><br>target | Object that [limits the audience](https://www.facebook.com/help/352402648173466) for this content. Anyone not in these demographics will not be able to view this content.<br><br>When used with a Live Online Event, this will apply to the event. |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> |     |
| `excluded_countries`[](#)<br><br>list<string> |     |
| `excluded_regions`[](#)<br><br>list<int64> |     |
| `excluded_cities`[](#)<br><br>list<int64> |     |
| `excluded_zipcodes`[](#)<br><br>list<string> |     |
| `timezones`[](#)<br><br>list<int64> |     |
| `age_min`<br><br>enum {13, 15, 18, 21, 25} |     |
| `title`<br><br>UTF-8 string | The title of the live video.<br><br>Supports Emoji |