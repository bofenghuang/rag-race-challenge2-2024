platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/

### Return Type

Struct {

`success`: bool,

} Or Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

## Updating

Update application information such as demographic restrictions.

### Permissions

* An app access token is required to update fields on an app.

### Example

To update an app restrictions, such as `age`, send a `POST` request to `/{app-id}`:

`curl -i -X POST "https://graph.facebook.com/{app-id}?restrictions={'age':'21+'}&access_token={app-access-token}"`

On success your app receives this response:

`{ "success": true }`

You can update an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) by making a POST request to [`/{application_id}`](https://developers.facebook.com/docs/graph-api/reference/application/).