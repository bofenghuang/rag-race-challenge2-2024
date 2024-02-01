platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-pages

### Search for Pages by Page ID

To search for Pages with specific Page IDs (obtained from the results of previous Page searches), create a search object using the `search_pages()` method with the `page_ids` parameter.

RPython

    # Create a search object limiting the response to specific Page IDs
    page_search <- client$search_pages(page_ids=['282820031228465'], fields='id,name,description')

    # Create a search object limiting the response to specific Page IDs
    page_search = client.search_pages(page_ids=['282820031228465'], fields='id,name,description')

For using Page IDs to search for posts from specific Facebook Pages, see [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts).