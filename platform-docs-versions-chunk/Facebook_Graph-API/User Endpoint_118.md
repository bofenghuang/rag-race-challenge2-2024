platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/permissions/

User permissions

# 

Returns a list of granted and declined permissions.

* * *

### Revoking Permissions

Apps can let people revoke permissions that were previously granted. For example, your app could have a settings page that lets someone disable publishing to Facebook. That settings page could also revoke the `publish_actions` permission at the same time.

You can revoke a specific permission by making a call to a Graph API endpoint:

DELETE /{user-id}/permissions/{permission-name}

This request must be made with a user access token or an app access token for the current app. If the request is successful, you will receive a response of `true`.

## Reading