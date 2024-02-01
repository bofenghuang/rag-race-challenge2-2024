platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-search-object


### Asynchronous search

Asynchronous searching capability is available for when you want to work with all of the data returned from a search, up to the search results limit that applies to every individual asynchronous search. Asynchronous searches can take some time (minutes to days) to complete because they return all of the data requested, not just one page at a time. However, because the search happens in the background, you don't have to wait for the results before submitting another search or doing other work. Once the search results are ready, you can fetch them.

The search result limit for each asynchronous search is 100,000 results. See [Estimating response size](#estimate).

Researcher Platform also has an asynchronous search feature, but that is strictly for static database use and does not work the same way. With Content Library API, you can only use the `async_search()` method described here.

When you submit an asynchronous search, the API returns "True" indicating the successful submission of the asynchronous query if the expected results are below the 100,000 search results limit, and an error message if the expected results are over the limit.

If the search is successfully submitted, you can check on the status and receive either IN\_PROGRESS or COMPLETE.

Use the `submit_async_query()` method with `async_status`:

RPython

    # Previous example submitted as an async search:
    async_submission <- new_post_search$submit_async_query()
    print(async_submission) # Returns True or error
    
    async_status <- new_post_search$get_async_search_status()
    print(async_status) # ex: # Returns IN_PROGRESS or COMPLETE

    # Previous example submitted as an async search:
    async_submission = new_post_search.submit_async_query()
    print(async_submission) # Returns "True" or an error
    
    async_status = new_post_search.get_async_search_status()
    print(async_status) # Returns IN_PROGRESS or COMPLETE

When the check for status shows COMPLETE, you can fetch the data in either JSON or DataFrame format (JSON is the default). You can also write the data to a file, which will be stored in the `/previous_searches/` folder in your Jupyter environment in JSON format.

RPython

    data <- new_post_search$get_data("dataframe") # Specifies DataFrame format
            
    new_post_search$write_data_to_file("file_name")  # Writes data to a file

    data = new_post_search.get_data("dataframe") # Specifies DataFrame format
            
    new_post_search.write_data_to_file("file_name") # Writes data to a file

Use the `get_all_async_queries()` method to get a list of all your previously executed asynchronous searches.

RPython

    # Get a list of search objects you've previously executed asynchronously:
    previous_searches <- client$get_all_async_queries()

    # Get a list of Search objects you've previously executed asynchronously:
    previous_searches = client.get_all_async_queries()
    print(previous_searches)