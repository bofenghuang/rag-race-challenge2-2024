platform: Facebook
topic: Graph-API
subtopic: Album Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Album Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/album/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The Album ID. |
| `backdated_time`<br><br>datetime | A user-specified time for when this object was created |
| `backdated_time_granularity`<br><br>enum | How accurate the backdated time is |
| `can_upload`<br><br>bool | Whether the app user can upload photos to this Album |
| `count`<br><br>unsigned int32 | The approximate number of [Photos](https://developers.facebook.com/docs/graph-api/reference/photo) and [Videos](https://developers.facebook.com/docs/graph-api/reference/video) in the Album. |
| `cover_photo`[](#)<br><br>[Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) | Album cover photo id |
| `created_time`<br><br>datetime | The Album creation date and time.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `description`<br><br>string | The Album description. |
| `event`[](#)<br><br>[Event](https://developers.facebook.com/docs/graph-api/reference/event/) | If this object has a place, the event associated with the place |
| `from`<br><br>User\|Page | The User who created the Album. |
| `link`<br><br>token with structure: URL | A link to this Album on Facebook. |
| `location`<br><br>string | The Album textual location. |
| `name`<br><br>string | The Album title.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `place`<br><br>[Place](https://developers.facebook.com/docs/graph-api/reference/place/) | Place info |
| `privacy`<br><br>string | The Album privacy settings. |
| `type`<br><br>string | The Album type: album, app, cover, profile, mobile, normal, or wall |
| `updated_time`<br><br>datetime | The date and time the Album was last updated. |