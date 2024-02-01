platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/rate-limiting


### Estimate response size for asynchronous queries

`get_estimate()` is a method that gives you a rough idea of how much data would be returned from a search you plan to run asynchronously. See [Estimating response size](https://developers.facebook.com/docs/content-library-api/guide-search-object#estimate) and [Asynchrounous search](https://developers.facebook.com/docs/content-library-api/guide-search-object#async-search) in the _Search Guide_ for more information on these topics.

**Points to keep in mind**:

* The API can only return up to 100,000 results from a single asynchronous search, so it can be helpful to know in advance if your search is likely to fail because the response size is too large.
    
* The query budget of 500,000 results in a rolling seven-day window can be used up quickly on just a few searches with high predicted results.
    

If the estimate comes out higher than 100,000, you might consider modifying the parameters to reduce the response size. You can continue to modify the search parameters and get new estimates until the search results are predicted to fall below the maximum allowed or close to the response size you prefer.

This is typically most useful for post searches because the number of results tend to be higher, but it can be used to estimate the number of results that would be returned by any search.

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