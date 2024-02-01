platform: Facebook
topic: Graph-API
subtopic: Image copyright Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Image copyright Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/image-copyright/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the object |
| `artist`<br><br>string | Artist/Photographer related the reference asset, user providedNote that the "Creator" field is used for image agencies or partners. |
| `copyright_monitoring_status`<br><br>enum | The status of the copyright reference file. It is used to determine if the match should be skipped. |
| `creation_time`<br><br>datetime | Creation time provided by TAO Server |
| `creator`<br><br>string | Creator of the reference asset, user provided |
| `custom_id`<br><br>string | Custom Id for reference asset, user provided |
| `description`<br><br>string | Description for reference asset, user provided |
| `filename`<br><br>string | Filename for reference asset, user provided |
| `image`<br><br>[Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) | The underlying image asset for the copyright |
| `matches_count`<br><br>unsigned integer | The number of matches for this copyright that are displayed in Rights Manager |
| `original_content_creation_date`<br><br>datetime | Date the reference asset was created, user provided |
| `ownership_countries`<br><br>VideoCopyrightGeoGate | Countries of included or excluded ownership for the given image copyright |
| `tags`<br><br>list<string> | Tags for the reference asset |
| `title`<br><br>string | The title of the copyright, generated from the reference asset |
| `update_time`<br><br>datetime | Update time provided by TAO Server |