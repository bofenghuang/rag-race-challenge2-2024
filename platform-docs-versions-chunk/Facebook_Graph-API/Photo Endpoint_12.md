platform: Facebook
topic: Graph-API
subtopic: Photo Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Photo Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/photo/

### Permissions

* To delete a User's photo, a User access token with `publish_actions`[permission](https://developers.facebook.com/docs/authentication/permissions/) is required.
    
* To delete a Page's photo a Page access token and `publish_pages`[permission](https://developers.facebook.com/docs/authentication/permissions/) is required.
    
* To delete a User's photo on a Page a Page access token is required.
    

You can delete a [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) by making a DELETE request to [`/{photo_id}`](https://developers.facebook.com/docs/graph-api/reference/photo/).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

}