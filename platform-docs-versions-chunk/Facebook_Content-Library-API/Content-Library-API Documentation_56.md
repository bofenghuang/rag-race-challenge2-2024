platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-posts


## Including multimedia in search results: Third-party cleanroom environment only

If you are using the Meta Content Library API in an approved third-party cleanroom environment (as opposed to Meta's Researcher Platform), _and if that environment supports it_, you have the option of including multimedia (photo, video) in your search results. Multimedia in posts from Facebook Pages, groups, and events are all eligible.

* Include the keyword `multimedia` in your query (`fields` parameter).
    
* For any media contained in a post, the response will include the type of media (photo, video), an ID, and either the media itself or a link to where the cleanroom environment has stored the media. Whether the media can be displayed directly in the response or not depends on the third-party cleanroom interface.
    
* The number of calls allowed that include multimedia is controlled by a multimedia query budget specific to the third-party cleanroom environment. See [Rate limiting and query budgeting for multimedia](https://developers.facebook.com/docs/content-library-api/rate-limiting#multimedia-query-limit) for more information.