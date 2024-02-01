platform: Facebook
topic: Graph-API
subtopic: Live video input stream Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Live video input stream Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/live-video-input-stream/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The ID of the input stream |
| `dash_ingest_url`<br><br>string | The dash ingest stream URL of this stream<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `dash_preview_url`<br><br>string | Preview URL for input to use with dash player<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `is_master`<br><br>bool | Set to true if this is input is being served to viewers<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `secure_stream_url`<br><br>string | The RTMPS URL for this stream<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `stream_health`<br><br>LiveVideoStreamHealth | Parameters indicating the input stream health<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `stream_id`<br><br>numeric string | 0-indexed ID for this ingest stream<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `stream_url`<br><br>string | The ingest RTMP URL for this stream<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |