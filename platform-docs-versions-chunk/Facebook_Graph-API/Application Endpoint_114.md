platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/permissions/

### Parameters

| Parameter | Description |
| --- | --- |
| `android_key_hash`<br><br>string | The app key hash for the Android app |
| `ios_bundle_id`<br><br>string | Bundle ID of the iOS app |
| `permission`<br><br>List<Permission> | Name of permission |
| `proxied_app_id`<br><br>int | App ID of the original app. The main Facebook apps act as a proxy and pass this ID along with their call |
| `status`<br><br>list<enum{live, unapproved}> | Default value: `Vec`<br><br>Status of permission |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ApplicationPermission](https://developers.facebook.com/docs/graph-api/reference/application-permission/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |