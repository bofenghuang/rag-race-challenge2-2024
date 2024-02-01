platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/rate-limiting


### Get your current usage

`get_query_budget()` is a method that displays your maximum number of data records retrieved per rolling 7-day period (query budget) and how much of that budget you have already used:

RPython

    library(contentlibraryapi)
    client <- ContentLibraryAPIClient$new(version='1')
            
    client$get_query_budget()

    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    client.get_query_budget()

This is a sample of the output:

 
\[{'current\_usage': 101000,
  'preallocated\_rows\_for\_running\_queries': 0,
  'total\_usage': 101000,
  'max\_usage\_limit': 500000,
  'timestamp': 'Tuesday, July 18, 2023 06:03:05 PM PDT'}\]

* _current\_usage_ is the number of results already returned by completed queries in the current 7-day rolling time window as of the current timestamp.
    
* _preallocated\_rows\_for\_running\_queries_ is the number of results (rows) allocated for asynchronous queries that are in progress.
    
* _total\_usage_ is the sum of _current\_usage_ and _preallocated\_rows\_for\_running\_queries_.
    
* _max\_usage\_limit_ is the maximum number of queries allowed in a 7-day rolling window.
    
* _timestamp_ marks the point in time at which these statistics were collected.
    

#### Current usage for multimedia

If you are using the Meta Content Library API in an approved third-party cleanroom environment (as opposed to Meta's Researcher Platform), _and if that environment supports including multimedia in posts_, multimedia-specific query budget usage is also available as a `multimedia` JSON object with the following fields:

* _total\_usage_ is the number of calls with multimedia in the current 7-day rolling time window as of the current timestamp.
    
* _max\_usage\_limit_ is the maximum number of calls with media allowed in a 7-day rolling window.
    

The query budget specific to queries containing multimedia is 1000 queries per 7-day rolling window.