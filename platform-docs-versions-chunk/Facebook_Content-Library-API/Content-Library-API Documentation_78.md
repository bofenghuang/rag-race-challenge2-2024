platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-search-object

### Response formats

By default, search responses use JavaScript Object Notation (JSON) format. This response format uses separators rather than being organized into columns. If you prefer the display in columns, the API has a function to specify DataFrame format instead.

RPython

    # Create a search object
    post_search <- client$search_posts(
        q='mountains')
            
    # Instructions for display:        
    print(post_search$query_next_page('dataframe'))

    # Create a search object
    post_search = client.search_posts(
        q='mountains')
    
    #Instructions for display:
    
    display(post_search.query_next_page('dataframe'))