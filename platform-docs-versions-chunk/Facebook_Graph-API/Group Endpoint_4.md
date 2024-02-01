platform: Facebook
topic: Graph-API
subtopic: Group Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Group Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/group


### Fields

| Property Name | Description | Type |
| --- | --- | --- |
| `id` | The Group ID | `string` |
| `cover` | Information about the Group's cover photo. | `CoverPhoto` |
| `id` | ID of the [Photo](https://developers.facebook.com/docs/reference/api/photo/) that represents this cover photo. | `string` |
| `source` | URL to the [Photo](https://developers.facebook.com/docs/reference/api/photo/) that represents this cover photo. | `string` |
| `offset_y` | The vertical offset in pixels of the photo from the bottom. | `int` |
| `offset_x` | The horizontal offset in pixels of the photo from the left. | `int` |
| `description` | A brief description of the Group. | `string` |
| `email` | The email address to upload content to the Group. Only current members of the Group can use this. | `string` |
| `icon` | The URL for the Group's icon. | `string` |
| `member_count` | The number of members in the Group. | `int` |
| `member_request_count` | The number of pending member requests. Requires an access token of an Admin of the Group.we The count is only returned when the number of pending member requests is over 50. | `int` |
| `name` | The name of the Group. | `string` |
| `owner` | _Deprecated in v9.0+. Will be deprecated in all versions February 9, 2021._ | `User` \| `Page` |
| `parent` | The parent of this Group, if it exists. | `Group` \| `Page` |
| `permissions` | The permissions a User has granted for an app installed in the Group. | `string` |
| `privacy` | The privacy setting of the Group. Possible values are `CLOSED`, `OPEN`, and `SECRET`. Requires an access token of an Admin of the Group. | `string` |
| `updated_time` | The last time the Group was updated (includes changes Group properties, Posts, and Comments). Requires an access token of an Admin of the Group. | `datetime` |