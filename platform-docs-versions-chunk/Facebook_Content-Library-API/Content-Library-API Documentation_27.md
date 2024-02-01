platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-pages


## search\_pages() method

This is the syntax of the `search_pages()` method:

search\_pages(
    q=Q,
    fields=FIELDS,    
    page\_ids=PAGE\_IDS,
    categories=CATEGORIES,
    is\_verified=IS\_VERIFIED,
    website=WEBSITE,
    admin\_countries=ADMIN\_COUNTRIES,
    since=SINCE,
    until=UNTIL
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search for. Searches a Page's `name` and `description` fields. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | Comma-separated list of Page fields you want included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-page) for descriptions of all available fields. |
| `PAGE_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library Page IDs as strings. Limits the query to the specified Pages. Maximum of 250 IDs. |
| `CATEGORIES`  <br>_Optional_ | List | Comma-separated list of categories to include in the search. |
| `IS_VERIFIED`  <br>_Optional_ | Boolean | The verification status of the Facebook Page. A Facebook Page with a verified badge indicates that Facebook has confirmed that it is the authentic presence for that person or brand. [Learn more](https://www.facebook.com/help/196050490547892). |
| `WEBSITE`  <br>_Optional_ | String | Website to match against the Facebook Page's "About" section. |
| `ADMIN_COUNTRIES`  <br>_Optional_ | List | Comma-separated list of countries by which to filter the Facebook Page's admin. Takes ISO Alpha-2 Country Code in 2-letter uppercase format. |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook Pages created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the Page.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook Pages created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the Page.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |