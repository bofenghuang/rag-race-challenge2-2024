platform: Facebook
topic: Graph-API
subtopic: Photo Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Photo Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/photo/

# Photo

Represents an individual photo on Facebook.

## Reading

This represents a Photo on Facebook.

### Permissions

* Any valid access token can read photos on a public Page.
    
* A page access token can read all photos posted to or posted by that Page.
    
* The current user's photos can be read if the user has granted the `user_photos` or `user_posts` permission.
    
* A user access token may read a photo that the current user is tagged in if they have granted the `user_photos` or `user_posts` permission. However, in some cases the photo's owner's privacy settings may not allow your application to access it.
    
* A User access token for an Admin of a Group can read Group-owned Photos.
    
* A User access token for an Admin of an Event can read Event-owned Photos if required after April 30, 2018.
    

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).