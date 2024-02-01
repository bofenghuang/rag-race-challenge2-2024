platform: Facebook
topic: Graph-API
subtopic: Group Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Group Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/group/albums

### Requirements

| Requirement | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Your app must be approved for the [Groups API](https://developers.facebook.com/docs/groups-api/) feature. |
| [App Installation](https://developers.facebook.com/docs/groups-api#app-installation) | The app must be installed on the Group. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token. |

### Fields

When requesting the following Album fields through field expansion, only Users who granted your app the `groups_access_member_info` permission will be included:

* `from`
* `likes`
* `reaction`