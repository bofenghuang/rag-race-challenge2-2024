platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-groups


### Request specific fields

To have the API return only specific fields on any groups in the response, create a search object using the `search_groups()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).

RPython

    # Create a search object including a list of fields:
    group_search <- client$search_groups(q='cybercrime', fields='id,name,description')        
    
    # Specify DataFrame response format:       
    print(group_search$query_next_page('dataframe'))

    # Create a search object including a list of fields:
    group_search = client.search_groups(q='cybercrime', fields='id,name,description')
    
    # Specify DataFrame response format:        
    display(group_search.query_next_page('dataframe'))

DataFrame response format has clear columns:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=3nXcV19g6AMAX9pkEeN&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDYqvuNhf4r7wLq-BYqKAWz5g9DkJb7e6Nd4tMrloKQjQ&oe=65BF473A)