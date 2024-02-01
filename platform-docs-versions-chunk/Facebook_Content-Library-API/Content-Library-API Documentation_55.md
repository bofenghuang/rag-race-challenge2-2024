platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-posts


### Search for Facebook posts containing a specific URL

To search for all public posts on Facebook Pages, groups, and events that contain specific keywords and a specific URL, create a search object using the `search_posts()` method with the `q` and `link` parameters. The `link` parameter cannot be used without the `q` parameter. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches are handled.

All forms of the URL that point to the same piece of content will be returned. Searching for multiple URLs in one query is not supported.

RPython

    # Create a search object including both the `q` and `link` parameters:
            
    post_search <- client$search_posts(q="nike", link="nike.com")
    print(post_search$query_next_page('dataframe'))

    # Create a search object including both the `q` and `link` parameters:
            
    post_search = client.search_posts(q="nike", link="nike.com")
    display(post_search.query_next_page('dataframe'))