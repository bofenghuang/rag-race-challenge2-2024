platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-groups


### Search for groups by group ID

You can search for Facebook groups using specific group IDs obtained from previous group searches.

To get data on specific Facebook groups that contain specific keywords or phrases, create a search object using the `search_groups()` method with the `q` parameter (specifying the keywords or phrases) and the `group_ids` parameter (specifying the list of group IDs you want included). If you omit the `q` argument, all groups in the list of IDs are included, not just those with a specific keyword or phrase.

RPython

    # Create a search object limiting the response to specific group IDs 
            group_search <- client$search_groups(q=`blackpink`, group_ids=[`753110959566351`], fields=`id,name,creation_date`)

    # Create a search object limiting the response to specific group IDs 
            group_search=client.search_groups(q=`blackpink`, group_ids=[`753110959566351`], fields=`id,name,creation_date`)

For using group IDs to search for posts from specific Facebook groups, see [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts).