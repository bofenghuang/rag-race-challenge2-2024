platform: Facebook
topic: Graph-API
subtopic: Comment Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Comment Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/comment

### New Page Experience

This API is supported for New Page Experience.

### Permissions

* A Page access token requested by a person who can perform the \`MODERATE\` task on the Page
    
* The `pages_read_engagement` permission
    
* The `pages_manage_engagement` permission
    

### Hiding Comments

You can hide most comments on Posts with the following exceptions:

* comments made by the Page
* comments made by the Page's admins
* comments made by the Page on a User's Post. The Post is owned by the User.
* comments made by any User on another User's Post to the Page. The Post is owned by the User.
* comments made by an Event creator. The Post is owned by the Event creator.
* comments made by a Facebook Group. The Post is owned by the Group.
* comments made by anyone on a review