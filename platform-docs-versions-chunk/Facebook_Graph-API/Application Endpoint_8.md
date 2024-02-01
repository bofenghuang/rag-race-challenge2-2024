platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/

### Parameters

| Parameter | Description |
| --- | --- |
| `app_version`<br><br>string | The version of the app being indexed<br><br>Required |
| `device_session_id`<br><br>string | Device session id of the uploading device |
| `extra_info`<br><br>string | Extra information about the app index |
| `platform`<br><br>enum {ANDROID, IOS} | The platform of the app being indexed<br><br>Required |
| `request_type`<br><br>enum {APP\_INDEXING, PLUGIN, BUTTON\_SAMPLING} | Default value: `"APP_INDEXING"`<br><br>Type of the app indexing request |
| `tree`<br><br>JSON object | The UI component tree of the app<br><br>Required |
| `screenname`<br><br>string |     |
| `screenshot`<br><br>string |     |
| `view`<br><br>list<JSON encoded app UI component> | Required |

### Return Type

Struct {

`success`: bool,

`is_app_indexing_enabled`: bool,

}