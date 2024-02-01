platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/upload


### Step 2: Initiate Upload

Initiate the upload session by sending a `POST` request to Graph API host address and append your upload session `{id}` along with the required headers indicated below. Upon success, a file handle, `{h}`, is returned that you can then use with any Graph API endpoints that support file handles returned by the Resumable Upload API.

If the upload session is taking longer than expected or has been interrupted, follow the steps described in the [Interruptions](#interruptions) section.

#### Request Syntax

POST https://graph.facebook.com/{api-version}/{upload-session-id}
  --header 'Authorization: OAuth {access-token}' 
  --header 'file\_offset: 0'
  --data-binary @{file-name}

**Placeholder Values**

* `{api-version}` — Graph API version.
* `{upload-session-id}` — Upload session ID returned in step 1.
* `{access-token}` — App user's User Access Token. The app user must have a role on the app that was targeted in step 1.
* `{file-name}` — Name of the file to upload.

You must include the access token in the header or your request will fail.

#### Response

{
  "h": "{h}"
}

Response property values:

* `{h}` — The uploaded file's file handle

#### Sample Request

curl -X POST \\
 "https://graph.facebook.com/`v19.0`/upload:MTphd..." \\
 --header "Authorization: OAuth EAAIT..." \\
 --header "file\_offset: 0" \\
 --data-binary @cats\_are\_jerks.png

#### Sample Response

{
    "h": "2:c2FtcGxl..."
}