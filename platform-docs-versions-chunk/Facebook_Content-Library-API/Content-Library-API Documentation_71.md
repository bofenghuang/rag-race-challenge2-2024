platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-ig-posts


### Search for posts from specific Instagram accounts

Searching for posts from specific Instagram accounts requires that you first obtain account IDs by creating a search object using the `search_ig_accounts()` method. The search results will include the ID field by default (you don't have to specify it in your query). See [Guide to Instagram accounts data](https://developers.facebook.com/docs/content-library-api/guide-ig-accounts) to learn about this method.

The IDs that are displayed are Meta Content Library IDs that protect user privacy and will not match the IDs of the content on Meta platforms. These Meta Content Library IDs are the ones you use in your subsequent post searches.

To search for posts from specific accounts, create a search object using the `search_ig_posts()` method with the `account_ids` parameter, and with or without the `q` parameter. `q` is not required but can be added to further filter posts. It does not matter when the posts were created. If you omit the `q` parameter, all public posts from the specified accounts are returned.

RPython

    # Create a search object for posts from specific account IDs        
    post_search <- client$search_ig_posts(account_ids='315242517956050')

    # Create a search object for posts from specific account IDs
    post_search = client.search_ig_posts(account_ids='315242517956050')