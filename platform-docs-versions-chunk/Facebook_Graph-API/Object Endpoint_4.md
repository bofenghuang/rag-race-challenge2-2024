platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/comments


### Limitations

* Other users' profile information and comments will not be returned when accessing user posts, photos, albums, videos, likes, and reactions unless authorized by those users.
    
* Comments returned in a query are based on default filtering. To get all comments that can be returned depending on your permissions, set the `filter` parameter to `stream` or use the `order` field.
    
* A [new Page](https://www.facebook.com/business/help/2752670058165459?id=418112142508425) can comment as the Page on new Pages or classic Pages. However, a classic Page can not comment on a new Page.
    
* For the following nodes, the `/comments` endpoint returns empty data if you read it with a [User access token](https://developers.facebook.com/docs/facebook-login/access-tokens):
    
    * [Album](https://developers.facebook.com/docs/graph-api/reference/album/)
        
    * [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/)
        
    * [Post](https://developers.facebook.com/docs/graph-api/reference/post/)
        
    * [Video](https://developers.facebook.com/docs/graph-api/reference/video/)
        
    
* The `id` field for the [`/PAGEPOST-ID/comments` endpoint](https://developers.facebook.com/docs/graph-api/reference/pagepost/) will no longer be returned for apps using the [Page Public Content Access feature](https://developers.facebook.com/docs/pages/overview/permissions-features#features). To access the comment IDs for a Page post you must be able to perform the [MODERATE task](https://developers.facebook.com/docs/pages/overview/permissions-features#tasks) on the Page being queried.
    
* For objects that have tens of thousands of comments, you may encounter limits while [paging](https://developers.facebook.com/docs/graph-api/using-graph-api#paging). Learn more about paging in our [Using the Graph API Guide](https://developers.facebook.com/docs/graph-api/using-graph-api).