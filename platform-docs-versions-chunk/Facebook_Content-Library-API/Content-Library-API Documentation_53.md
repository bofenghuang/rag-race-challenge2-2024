platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-posts


### Search for posts from specific Facebook Pages, groups, or events

Searching for posts from specific Facebook Pages, groups, or events requires that you first obtain Page, group, or event IDs by creating search objects using the `search_pages()`, `search_groups()`, or `search_events()` methods. The search results will include the ID field by default (you don't have to specify it in your query). See [Guides](https://developers.facebook.com/docs/content-library-api/guides) to learn about these methods.

The IDs that are displayed in the search results are Meta Content Library IDs that protect user privacy and will not match the IDs of the content on Meta platforms. These Meta Content Library IDs are the ones you use in your subsequent post searches.

To search for posts from specific Pages, groups, or events, create a search object using the `search_posts()` method with the `page_ids`, `group_ids`, or `event_ids` parameter, and with or without the `q` parameter. `q` is not required but can be added to further filter posts. It does not matter when the posts were created. If you omit the `q` parameter, all public posts on the specified Pages, groups, or events are returned.

RPython

    # Create a search object for posts from specific Page IDs        
    post_search <- client$search_posts(page_ids='282820031228465')

    # Create a search object for posts from specific Page IDs
    post_search = client.search_posts(page_ids='282820031228465')

RPython

    # Create a search object for posts from specific group IDs        
    post_search <- client$search_posts(group_ids='634974087068385')

    # Create a search object for posts from specific group IDs
    post_search = client.search_posts(group_ids='634974087068385')

RPython

    # Create a search object for posts from specific event IDs        
    post_search <- client$search_posts(event_ids='1025592588867344')

    # Create a search object for posts from specific event IDs
    post_search = client.search_posts(event_ids='1025592588867344')

RPython

    # Create a search object that combines searching for posts from specific Page IDs and specific group IDs       
    post_search <- client$search_posts(page_ids='282820031228465', group_ids='634974087068385')

    # Create a search object that combines searching for posts from specific Page IDs and specific group IDs 
    post_search = client.search_posts(page_ids='282820031228465', group_ids='634974087068385')