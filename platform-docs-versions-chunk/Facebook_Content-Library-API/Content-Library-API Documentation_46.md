platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-events


### Search for events by event ID

You can search for Facebook events using specific event IDs obtained from previous event searches.

To get data on specific Facebook events that contain specific keywords or phrases, create a search object using the `search_events()` method with the `q` parameter (specifying the keywords or phrases) and the `event_ids` parameter (specifying the list of event IDs you want included). If you omit the `q` argument, all events in the list of IDs are included, not just those with a specific keyword or phrase.

RPython

    # Create a search object limiting the response to specific event IDs
    event_search <- client$search_events(event_ids=['284083459792042'], fields='id,name,description,picture{url}')

    # Create a search object limiting the response to specific event IDs
    event_search = client.search_events(event_ids=['284083459792042'],  fields='id,name,creation_time')

For using event IDs to search for posts from specific Facebook events, see [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts).