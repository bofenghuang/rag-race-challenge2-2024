platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/changelog


## Version 2.0, January 30 2024

Meta Content Library API v2.0 has been enhanced with the following new features:

* You can now search Facebook and Instagram posts by post ID. Use the `post_ids` parameter, specifying one or more post IDs that you obtained from a previous search. See [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts) and [Guide to Instagram posts data](https://developers.facebook.com/docs/content-library-api/guide-ig-posts).
    
* A subset of Instagram personal accounts that match qualification criteria can now be included in results when you search for Instagram account information or for posts from Instagram accounts. Public Instagram accounts include professional accounts for businesses and creators. They now also include a subset of personal accounts that have account privacy set to public and have either a verified badge or 50,000 or more followers. A verified badge in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. See [Guide to Instagram accounts data](https://developers.facebook.com/docs/content-library-api/guide-ig-accounts) and [Guide to Instagram posts data](https://developers.facebook.com/docs/content-library-api/guide-ig-posts).
    
* You can now filter posts from Facebook Pages by the page admin’s location country. Set the new `admin_countries` parameter to include one or more country codes of your choice. See [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts).
    
* Multimedia (photos and videos) can now be included in search post results for both Instagram and Facebook. This feature is only available if you are accessing the API in an approved third party cleanroom environment, and only if that environment supports retrieval of multimedia. The feature is not available in Researcher Platform. See [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts) and [Guide to Instagram posts data](https://developers.facebook.com/docs/content-library-api/guide-ig-posts).
    
* The citation format was updated with a new Digital Object Identifier (DOI) that specifies version 2.0. Older release DOIs are still available for reference. See [Citations](https://developers.facebook.com/docs/content-library-api/citations).