platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/


### Parameters

| Parameter | Description |
| --- | --- |
| `mappings`<br><br>array<JSON object> | The event to UI component mappings of the app<br><br>Required |
| `method`<br><br>enum {INFERENCE, MANUAL, CONFIRMED\_INFERENCE, BUTTON\_INDEXING, UNKNOWN} | method<br><br>Required |
| `event_name`<br><br>string | event\_name<br><br>Required |
| `event_type`<br><br>enum {CLICK, SELECTED, TEXT\_CHANGED} | event\_type<br><br>Required |
| `app_version`<br><br>string | app\_version<br><br>Required |
| `parameters`<br><br>array<JSON object> | parameters |
| `name`<br><br>string | name<br><br>Required |
| `path`<br><br>array<JSON object> | path<br><br>Required |
| `class_name`<br><br>string | class\_name<br><br>Required |
| `index`<br><br>int64 | index<br><br>Required |
| `id`<br><br>int64 | id  |
| `text`<br><br>string | text |
| `tag`<br><br>string | tag |
| `description`<br><br>string | description |
| `hint`<br><br>string | hint |
| `match_bitmask`<br><br>int64 | match\_bitmask |
| `path_type`<br><br>enum {ABSOLUTE, RELATIVE} | Default value: `"ABSOLUTE"`<br><br>path\_type |
| `component_id`<br><br>string | component\_id<br><br>Required |
| `path`<br><br>array<JSON object> | path<br><br>Required |
| `class_name`<br><br>string | class\_name<br><br>Required |
| `index`<br><br>int64 | index<br><br>Required |
| `id`<br><br>int64 | id  |
| `text`<br><br>string | text |
| `tag`<br><br>string | tag |
| `description`<br><br>string | description |
| `hint`<br><br>string | hint |
| `match_bitmask`<br><br>int64 | match\_bitmask |
| `component_id`<br><br>string | component\_id<br><br>Required |
| `path_type`<br><br>enum {ABSOLUTE, RELATIVE} | Default value: `"ABSOLUTE"`<br><br>path\_type |
| `screenshot_handle`<br><br>string | screenshot\_handle |
| `dimensions`<br><br>array<JSON object> | dimensions |
| `top`<br><br>int64 | top<br><br>Required |
| `left`<br><br>int64 | left<br><br>Required |
| `width`<br><br>int64 | width<br><br>Required |
| `height`<br><br>int64 | height<br><br>Required |
| `activity_name`<br><br>string | activity\_name |
| `mutation_method`<br><br>enum {REPLACE, ADD, DELETE} | Detailed mutation type like replace, add<br><br>Required |
| `platform`<br><br>enum {ANDROID, IOS} | The platform of the app being indexed<br><br>Required |
| `post_method`<br><br>enum {EYMT, CODELESS} | Default value: `"CODELESS"`<br><br>Whether the api is called by codeless or EYMT |