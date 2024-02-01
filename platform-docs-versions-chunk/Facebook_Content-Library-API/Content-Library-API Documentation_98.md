platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/rate-limiting

# Rate limiting and query budgeting

Meta Content Library and API both have limits at the individual researcher level that:

* Put a cap on the number of queries allowed per user per minute (a separate limit for each tool). This is called a _rate limit_.
    
* Put a cap on the number of retrieved data records (posts, for example) per user per seven-day rolling window. This limit, called a _query budget_, is shared between the two tools per user. In other words, a single researcher has a total query budget between the two tools, regardless if they are using just Content Library, just Content Library API, or both.
    

Maintaining a rate-limiting and query-budgeting policy ensures that the tools run efficiently and provide all users with consistent data access, unhindered by reduced performance. It also provides a measure of protection against system flooding.

## What are the limits?

### Rate limits for Content Library

* 60 queries over any one-minute interval