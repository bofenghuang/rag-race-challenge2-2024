platform: Facebook
topic: Graph-API
subtopic: Group Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Group Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/group

### Permissions

* `groups_access_member_info` — Enables your app to receive member-related data on group content.
* `publish_to_groups` — Enables your app to post content into a group on behalf of a user.

**For Public and Closed Groups**

A User access token

**For Secret Groups**

A User access token for an Admin of the Group

**Caveats**

* Fields that return User information will not be included in any responses unless the request is made using an access token of an Admin of the Group.