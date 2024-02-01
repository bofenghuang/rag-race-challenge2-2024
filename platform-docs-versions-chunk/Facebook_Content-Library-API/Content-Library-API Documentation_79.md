platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-search-object

### Altering search parameters

While exploring the data to arrive at the most appropriate search parameters for your purposes, you might find the `alter_search_params` method useful. This method returns a new search object with any new parameters you specify overriding the original ones.

RPython

    # Get a new search object with altered parameters:
    new_post_search <- post_search$alter_search_params(q = 'mountains', lang='en,es', since=1622937600,
        until=1622938000)
    
    # Instructions for display:
    new_post <- new_post_search$query_next_page()
    print(new_post)

    # Get a new search object with altered parameters:
    new_post_search = post_search.alter_search_params(q = 'mountains', lang='en,es', since=1622937600,
        until=1622938000)
    
    # Instructions for display:
    new_post = new_post_search.query_next_page()
    print(new_post)