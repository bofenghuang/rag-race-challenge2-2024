platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-ig-posts

### Search for posts by post ID

To search for posts with specific post IDs (that you obtained from a previous post search), create a search object using the `search_ig_posts()` method with the `post_ids` parameter specifying a list of post IDs to include in the results.

RPython

    # Create a search object for posts with specific post IDs        
    post_search <- client$search_ig_posts(post_ids='7069734086407812')

    # Create a search object for posts with specific post IDs
    post_search = client.search_ig_posts(post_ids='7069734086407812')