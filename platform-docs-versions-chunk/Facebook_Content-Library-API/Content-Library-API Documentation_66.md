platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-ig-posts


## search\_ig\_posts() method

This is the syntax of the `search_ig_posts()` method:

search\_ig\_posts(
    q=Q,
    fields=FIELDS,
    post\_ids=POST\_IDS,
    account\_ids=ACCOUNT\_IDS,
    account\_types=ACCOUNT\_TYPES,
    lang=LANG,
    is\_branded\_content=IS\_BRANDED\_CONTENT,
    media\_types=MEDIA\_TYPES,
    views\_bucket\_start=VIEWS\_BUCKET\_START,
    views\_bucket\_end=VIEWS\_BUCKET\_END
    since=SINCE,
    until=UNTIL  
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search for. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | Comma-separated list of Instagram post fields to be included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-post) for descriptions of all available fields. |
| `POST_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library post IDs to include in search results. Limits the query to posts in the list. Maximum of 250 IDs. |
| `ACCOUNT_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library account IDs as strings. Limits the query to posts from accounts in the list. Maximum of 250 IDs. |
| `ACCOUNT_TYPES`  <br>_Optional_ | List | Comma-separated list of Instagram account types. Possible values are `creator`, `business`, and `personal`.<br><br>Public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT3QoL3W6TXSG-rxoFyWdvY1FWS2zX5Xi7-blR4fL0-AkeYXErMTqxi0khY6KKm4ju5_nQl73xB8cXV6cQ3bjaKN206RrM9HiqoBjKgtOT2z-5Gfvjbqw3zRUreHEMIQq3f7xMDJkHDkq9wlaKIr2tXBOjNgBQ) and have either a verified badge or 50,000 or more followers. A [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT20UeaFdNTDQxXvreLoOj6SY6ueVf9hJdJUXdfPJgkJofAasKbFZkYJXWYeTkj6ycgymUOwqoi2ZmYMs2MRq8IZo6nnv0KzjlzikTeISTfwpX5scYGC76DT-djT4LTM2Sa7cJwVfdHKnCmY) in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. |
| `LANG`  <br>_Optional_ | String | The content languages of the Instagram posts to include, specified as ISO 639-1 language codes in 2-letter lowercase format. Multiple languages are comma-separated either in a single string (`lang="ru,es"`) or in an array (`lang=["ru" "es"]`). |
| `IS_BRANDED_CONTENT`  <br>_Optional_ | Boolean | Indicates whether the Instagram posts returned can include branded content or not. [Learn more](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1123581461537025%2F%3Fhelpref%3Dsearch%26query%3Dbrand%2520content%26search_session_id%3Df7d00d14670ab93e032d827b36e54ff3%26sr%3D1&h=AT3fwepWxJp-cxYUp1rxlOH0M0J21ye4eITf4G1b2tT4ngh7Em3ufO4_NkYnl6MIDc_15Y1cBlzQ7uf70E1yNydCP9-d0qx7odBmkw055rxEEJFaSH0QeZoVlUGZRtx7abJn8j8fWyv2P7kh). |
| `MEDIA_TYPES`  <br>_Optional_ | List | Comma-separated list of media types to be included in the search results. Media types include `albums`, `photos`, and `videos` (including reels). |
| `VIEWS_BUCKET_START`  <br>_Optional_ | Integer | Instagram posts with view counts larger than or equal to this number match the search criteria. Range is from 0 to the maximum of more than 100 million.<br><br>  <br><br>Views are the number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-post) for more details. |
| `VIEWS_BUCKET_END`  <br>_Optional_ | Integer | Instagram posts with view counts smaller than or equal to this number match the search criteria. Range is from 0 to the maximum of more than 100 million.<br><br>  <br><br>Views are the number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-post) for more details. |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram posts created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who made the post.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram posts created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who made the post.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |