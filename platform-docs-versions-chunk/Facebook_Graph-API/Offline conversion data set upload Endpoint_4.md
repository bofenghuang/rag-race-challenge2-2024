platform: Facebook
topic: Graph-API
subtopic: Offline conversion data set upload Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Offline conversion data set upload Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/offline-conversion-data-set-upload/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | ID of the data set upload<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `api_calls`<br><br>int32 | Api calls stat from RTCS |
| `creation_time`<br><br>int32 | Time of the creation of this upload tag |
| `duplicate_entries`<br><br>int32 | Duplicate entries stat |
| `event_stats`<br><br>string | Event stats |
| `event_time_max`<br><br>integer | Latest entry timestamp |
| `event_time_min`<br><br>integer | First entry timestamp |
| `first_upload_time`<br><br>int32 | Time of the first upload to this upload tag |
| `is_excluded_for_lift`<br><br>bool | The flag to determine if the upload data should be excluded from Lift<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `last_upload_time`<br><br>int32 | Time of the most recent upload to this upload tag |
| `match_rate_approx`<br><br>int32 | Approximate match rate percentage for the entries in this upload |
| `matched_entries`<br><br>int32 | Matched entries stat |
| `upload_tag`<br><br>string | The name by which uploads are grouped in this data set<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `valid_entries`<br><br>int32 | Valid entries stat |