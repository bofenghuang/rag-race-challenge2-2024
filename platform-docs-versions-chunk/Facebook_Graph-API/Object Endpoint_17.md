platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/likes

### Permissions

* A Page access token requested by a person who can perform the [`CREATE_CONTENT` task](https://developers.facebook.com/docs/pages/overview-1#tasks) on the Page
    
* The `pages_manage_engagement` permission
    

### Limitations

* The Page must also be able to like the object (whether via API or on Facebook.com).
    
* The object must not have already been liked by the Page.
    
* If the Page has already reacted to an object (wow, sad) then a like will succeed, but the reaction will not change.
    
* Liking a Page review is not supported.
    

### Fields

No fields are required to add likes.

### Response

On success, your app will receive the following response:

{
  "success": true
}

## Updating

You can't perform this operation on this endpoint.