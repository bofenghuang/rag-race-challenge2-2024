platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/likes

### Limitations

* Only aggregated counts using `total_count` with the `summary` parameter are available for Post likes.
    
* The `like` reaction counts include both "like" and "care" reactions.
    
* `total_count` represents the approximate number of likes, however, the actual number returned might be different depending on privacy settings.
    
* The `GET /{group-post-id}/likes` and `GET /{post-id}/likes` endpoints are deprecated in v8.0+ and deprecated in all versions on Nov. 2, 2020.
    

### Fields

| Property Name | Description | Type |
| --- | --- | --- |
| `total_count` | Total number of User and Page likes on the object. To have this field returned, you must include the `summary=true` parameter and value in your request. | `int32` |