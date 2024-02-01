platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-search-object


### Estimating response size

Use the `get_estimate()` function to get a rough idea of how much data would be returned from a search you have defined. Since the API can only return up to 100,000 results from a single asynchronous search, it can be helpful to know in advance if your search is likely to fail because the response size is too large. If the estimate comes out higher than 100,000, consider modifying the parameters to reduce the response size. You can continue to modify the search parameters and get new estimates until the search results are predicted to fall below the maximum allowed.

This is typically most useful for post searches because the number of results tend to be higher, but it can be used to estimate the size of data that would be returned by any search.

RPython

    # Request an estimate:
    post_search <- client$search_posts(q = 'dogs')
    estimate <- post_search$get_estimate()
            
    # Display the estimate:        
    print(estimate)

    # Request an estimate:  
    post_search = client.search_posts(q='dogs')
    estimate = post_search.get_estimate()
          
    # Display the estimate:        
    print(estimate)