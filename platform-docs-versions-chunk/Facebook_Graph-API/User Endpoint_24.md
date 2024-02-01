platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/accounts/

### Permissions

* A User access token with `pages_manage_metadata` and `pages_show_list` permissions.
    
* The `category_enum` parameter with a Page Category.
    
* Other requirements vary depending on the type of page you are creating but may require the following parameters: `name`, `about`, `picture`, and `cover_photo`.
    

**Note:** When setting the locale, at least one, `city_id`, `location`, or `coordinates`, is required. Caveats:

* `city_id` and `location` can not be used together
    
* `city_id` and `coordinates` can be used together however the coordinates must be within the city selected
    
* `location` and `coordinates` can be used together however the coordinates must be within the location selected