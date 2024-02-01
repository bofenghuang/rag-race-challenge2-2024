platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/quick-start

## Test with a basic search

Test your setup by running a basic search query. Here's an example to try:

RPython

    # Create a search object
    my_page_search <- client$search_pages(
        q='mountains')
            
    #Instructions for display:        
    pages <- my_page_search$query_next_page()
    print(pages)

    # Create a search object
    my_page_search = client.search_pages(
        q='mountains')
    
    #Instructions for display:
    pages = my_page_search.query_next_page()
    print(pages)