platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/uploads/

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) or [System User](https://developers.facebook.com/docs/marketing-api/system-users/overview#system-user-access-token). The app user who granted the token must have an Administrator or Developer [role](https://developers.facebook.com/docs/development/build-and-test/app-roles) on the app. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | None. |

You can make a POST request to `uploads` edge from the following paths:

* [`/{application_id}/uploads`](https://developers.facebook.com/docs/graph-api/reference/application/uploads/)

When posting to this edge, no Graph object will be created.