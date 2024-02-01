platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/upload


### Step 1: Create a Session

Send a `POST` request that describes your file to the [Application Uploads](https://developers.facebook.com/docs/graph-api/reference/application/uploads/) endpoint (`{app-id}/uploads`) . Upon success an upload session ID will be returned that you can use in the next step to initiate the upload.

#### Request Syntax

POST https://graph.facebook.com/{api-version}/{app-id}/uploads
  &file\_length={file-length}
  &file\_type={file-type}
  &access\_token={access-token}

Parameters Placeholders:

* `{api-version}` — The Graph API version.
* `{app-id}` — The application ID. The uploaded file that will be associated with this app. The app user must have an administrator or developer role on this app.
* `file-length` — The file's size, in bytes.
* `file-type` — The file's MIME type. Valid values are: `application/pdf`, `image/jpeg`, `image/jpg`, `image/png`, and `video/mp4`
* `{access-token}` — The app user's User Access Token.

Refer to the [Application Uploads](https://developers.facebook.com/docs/graph-api/guides/docs/graph-api/reference/application/uploads/) endpoint reference for a complete list of available query parameters and supported file types.

#### Response

{
  "id": "{id}"
}

Response property values:

* `{id}` — Upload session ID.

#### Sample Request

curl -X POST \\
 "https://graph.facebook.com/`v19.0`/584544743160774/uploads?file\_length=109981&file\_type=image/png&access\_token=EAAIT..."

#### Sample Response

{
    "id": "upload:MTphd..."
}