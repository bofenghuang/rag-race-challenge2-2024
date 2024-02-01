platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-search-object


### Basic synchronous search with paginated results

Unless you specify otherwise, a search object is synchronous in nature, meaning that you submit the query and wait for the results, and you cannot submit another until the first one finishes. Synchronous search results display 10 results at a time (a "page") and you request the next pages one by one. This type of search is most useful when the data matching the search criteria is expected to be small or when you just want to sample some results to see if they are appropriate for your research and don't necessarily need to see everything. This can be a step in the process of fine-tuning your search criteria.

Synchronous searches can return a maximum of 1000 results. When you need a larger set of results, use [asynchronous searches](#async-search).

RPython

    #Import the client library if you have not already done so:        
    library(contentlibraryapi)
    client <- ContentLibraryAPIClient$new(version='2')
    
    # Create a search object using the search_posts() search method:
    post_search <- client$search_posts(
        q='mountains',
        since=1622937600,
        until=1686095999)
            
    # Instructions for display:        
    posts <- post_search$query_next_page()
    print(posts)

    #Import the client library if you have not already done so:
    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    # Create a search object using the search_posts() search method:
    post_search = client.search_posts(
        q='mountains',
        since=1622937600,
        until=1686095999)
            
    #Instructions for display:        
    posts = post_search.query_next_page()
    print(posts)