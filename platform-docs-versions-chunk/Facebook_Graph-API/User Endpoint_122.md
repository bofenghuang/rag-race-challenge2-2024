platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/photos/

# User Photos

Photos for a person.

## Reading

Query photos that the user tagged in / uploaded

### Uploaded Photos

By default reading from the `photos` edge includes all photos a person has been tagged in.

When you read a person's Photos you can also include an optional `type` parameter with the value `uploaded` to get only the list of photos that a person has uploaded:

GET /{user-id}/photos?type=uploaded

You can also use this form to add the type, but the `type=uploaded` form is preferred:

GET /{user-id}/photos/uploaded

### Permissions

* For any photos uploaded by someone, and any photos in which they have been tagged - A user access token for that person with `user_photos` permission.