platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-posts


## search\_posts() method

This is the syntax of the `search_posts()` method:

search\_posts(
    q=Q,
    fields=FIELDS,
    post\_ids=POST\_IDS,
    page\_ids=PAGE\_IDS,
    group\_ids=GROUP\_IDS,
    event\_ids=EVENT\_IDS,
    lang=LANG,
    link=LINK,
    is\_branded\_content=IS\_BRANDED\_CONTENT,
    admin\_countries=ADMIN\_COUNTRIES,
    owner\_types=OWNER\_TYPES,
    views\_bucket\_start=VIEWS\_BUCKET\_START,
    views\_bucket\_end=VIEWS\_BUCKET\_END
    since=SINCE,
    until=UNTIL      
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search for. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | Comma-separated list of Facebook post fields you want included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-post) for descriptions of all available fields. |
| `POST_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library post IDs as strings. Limits the query to posts in the list. Maximum of 250 IDs. |
| `PAGE_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library Page IDs as strings. Limits the query to posts from Pages in the list. Maximum of 250 IDs. |
| `GROUP_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library group IDs as strings. Limits the query to posts from groups in the list. Maximum of 250 IDs. |
| `EVENT_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library event IDs as strings. Limits the query to posts from events in the list. Maximum of 250 IDs. |
| `LANG`  <br>_Optional_ | String | The content languages of the Facebook posts to include, specified as ISO 639-1 language codes in 2-letter lowercase format. Multiple languages are comma-separated either in a single string (`lang="ru,es"`) or in an array (`lang=["ru" "es"]`). |
| `LINK`  <br>_Optional with the `q` parameter_ | String | Posts containing the specified URL are included in search results. All forms of the URL that point to the same piece of content will be returned.<br><br>  <br><br>Usage:<br><br>* Can only be used with the `q` parameter.<br>* Returns posts from exact matches only.<br>* Searching for multiple URLs in one query is not supported.<br><br>**If you want to search all posts from a domain, the `link` parameter is not the best option since it returns posts from exact matches only.**<br><br>Instead, you can use the `q` parameter where q=_url_. Results would include all posts in which the value of `q` is at least a part of the URL in the post. For example, posts from cnn.com/entertainment would be included in a search for cnn.com. Once you have the larger set of results, you can write Python or R code in your Jupyter environment to narrow them down. |
| `IS_BRANDED_CONTENT`  <br>_Optional_ | Boolean | Indicates whether the Facebook posts returned can include branded content or not. [Learn more](https://www.facebook.com/business/help/788160621327601?id=1912903575666924&content_id=OESWySYCNR5UDZX&ref=sem_smb&utm_term=dsa-1731453251743&gclid=CjwKCAjwtuOlBhBREiwA7agf1uNvtkdQIU-GlDHtOVsq1r2PAFq7Z7QFVqHPf4QsH54oi0soVculuxoCMHMQAvD_BwE). |
| `ADMIN_COUNTRIES`  <br>_Optional_ | List | Comma-separated list of countries by which to filter posts from Facebook Pages using the Page admin's country location. Only returns posts for which `owner_types = page`, whether or not the `owner_types` parameter has been set. Takes ISO Alpha-2 Country Code in 2-letter uppercase format. |
| `OWNER_TYPES`  <br>_Optional_ | List | Comma-separated list of owner types to be included in the search results. Possible values are `page`, `group` and `event`. |
| `VIEWS_BUCKET_START`  <br>_Optional_ | Integer | Facebook posts with view counts larger than or equal to this number match the search criteria. Range is from 0 to the maximum of more than 100 million. Used with `VIEWS_BUCKET_END` to define a range.<br><br>  <br><br>Views are the number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. See [Data Dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-post) for more details. |
| `VIEWS_BUCKET_END` _Optional_ | Integer | Facebook posts with view counts smaller than or equal to this number match the search criteria. Range is from 0 to the maximum of more than 100 million. Used with `VIEWS_BUCKET_START` to define a range.<br><br>  <br><br>Views are the number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-post) for more details. |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook posts created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who made the post.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook posts created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who made the post.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |