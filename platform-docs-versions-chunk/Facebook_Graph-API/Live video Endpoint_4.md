platform: Facebook
topic: Graph-API
subtopic: Live video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Live video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/live-video/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The live video ID. |
| `ad_break_config`<br><br>LiveVideoAdBreakConfig | The ad break configurations for clients implementing triggering an ad break ui. Contains ad break eligibility and constants to render the ui. In order to use this, the page hosting the broadcast needs to be whitelisted. |
| `ad_break_failure_reason`<br><br>enum | Ad Break failure reason |
| `broadcast_start_time`<br><br>datetime | The time the video was initially published |
| `copyright`<br><br>[VideoCopyright](https://developers.facebook.com/docs/graph-api/reference/video-copyright/) | The copyright information for the live video |
| `creation_time`<br><br>datetime | The creation time of the live video |
| `dash_ingest_url`<br><br>string | The dash ingest stream URL of the live video |
| `dash_preview_url`<br><br>string | Preview URL for dash player |
| `description`<br><br>string | The description of the live video |
| `embed_html`<br><br>iframe\_with\_src | The embed html of the live video<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `from`<br><br>User\|Page | The originator of the live video |
| `ingest_streams`<br><br>[list<LiveVideoInputStream>](https://developers.facebook.com/docs/graph-api/reference/live-video-input-stream/) | Individual ingest streams. |
| `is_manual_mode`<br><br>bool | Whether schedule live is in manual mode, in which live video will start manually instead of on schedled time |
| `is_reference_only`<br><br>bool | Whether the live video is exclusively used for copyright monitoring |
| `live_views`<br><br>unsigned int32 | The instant viewer count of the live video now |
| `overlay_url`<br><br>string | A URL used in conjunction with Facebook Live Producer to show overlays for this broadcast. In order to use this, the page hosting the broadcast needs to be whitelisted. |
| `permalink_url`<br><br>uri | The permalink URL of this video on Facebook. |
| `planned_start_time`<br><br>datetime | Planned start time for a live video |
| `recommended_encoder_settings`<br><br>LiveVideoRecommendedEncoderSettings | Recommended encoder settings for this live video. |
| `seconds_left`<br><br>int32 | Seconds left in the maximum possible duration for this live video |
| `secure_stream_url`<br><br>string | The secure stream url of the live video. Check with your encoder whether this is supported before adapting<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `status`<br><br>enum | The status of the LiveVideo.<br><br>A `LIVE_NOW` LiveVideo is one that will be published to the intended destination (Timeline, Group, Page, etc) upon receiving valid video data, or one that is already published and actively streaming.<br><br>An `UNPUBLISHED` LiveVideo is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state.<br><br>A `SCHEDULED_UNPUBLISHED` LiveVideo is scheduled to go live at a future time.<br><br>A `SCHEDULED_LIVE` LiveVideo is one whose scheduled time has passed, yet the stream is not yet live. Either in the process of transitioning, or still waiting for a valid video stream.<br><br>(Consider using the `SCHEDULED` states to create a planned, future LiveVideo.)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `stream_url`<br><br>string | The stream url of the live video<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `targeting`<br><br>LiveVideoTargeting | Targeting information for this live video |
| `title`<br><br>string | The title of the live video<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `video`<br><br>[Video](https://developers.facebook.com/docs/graph-api/reference/video/) | The inside video of the live video |