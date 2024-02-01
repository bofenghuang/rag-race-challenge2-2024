platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-pages


### Search for Pages by keyword

To search for Pages that contain a specific keyword, create a search object using the `search_pages()` method with the `q` parameter. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches are handled.

RPython

    # Create a client object if you have not already done so:
    library(contentlibraryapi)
    client <- ContentLibraryAPIClient$new(version='2')
            
    # Create a search object:
    page_search <- client$search_pages(q='cybercrime')        
    
    # No results are displayed until you provide display instructions:        
    print(page_search$query_next_page())

    # Create a client object if you have not already done so:
    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    # Create a search object:
    page_search = client.search_pages(q='cybercrime')
            
    # No results are displayed until you provide display instructions:
    display(page_search.query_next_page())

This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) for other display and storage options.