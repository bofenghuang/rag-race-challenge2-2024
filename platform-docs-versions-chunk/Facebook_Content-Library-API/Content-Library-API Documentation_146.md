platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/get-api-code

# Get API Code

Get API Code is a tool within Meta Content Library that automatically generates a Python or R code snippet corresponding to your current search that you can copy and paste into your Meta Content Library API Jupyter notebook.

**Remember the limits**

If you submit a synchronous query in the Content Library API that would return more than 1000 results, you will only see the top 1000.

If you submit an asynchronous query in the API that would return more than 100,000 results, the API will give you an error message and will not complete the query.

The automatically generated R or Python code might return more than 100,000 results. Be sure to check the very top of the Content Library search results to see the size of the results before you use the same search in the API.

## In Content Library