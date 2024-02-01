platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/rate-limiting

### Rate limits for Content Library API

* Synchronous search queries: 60 queries over any one-minute interval
    
* Asynchronous search queries: 1 query per minute
    

See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) for information about the difference between synchronous and asynchronous searches.

### Combined query budget per researcher

For Content Library and API combined, you can retrieve a maximum of 500,000 data records per seven-day rolling window. The rolling window is one week previous to the current timestamp (to the second). If you are blocked by hitting the query budget, you should not need to wait long before you try again.

If you are using the Content Library API in a third-party cleanroom environment, and if that environment supports including multimedia in posts, there is an additional query budget of 1000 queries with multimedia per rolling week.