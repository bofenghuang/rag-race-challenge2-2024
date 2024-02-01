platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/field-expansion

## Specifying multiple fields

You can specify which multiple fields you want returned on any associated data by using the `fields` parameter, with the field names separated by commas.

RPython

    library(contentlibraryapi)
    client <- ContentLibraryAPIClient$new(version='1')
            
    post_search <- client$search_posts(q='cybercrime', fields="id,text")
    post_search$query_next_page()

    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version='1')
    
    
    post_search = client.search_posts(q="cybercrime", fields="id,text")
    display(post_search.query_next_page())