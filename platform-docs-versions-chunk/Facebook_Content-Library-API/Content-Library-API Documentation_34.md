platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-fb-groups


## search\_groups() method

This is the syntax of the `search_groups()` method:

search\_groups(
    q=Q
    fields=FIELDS,
    group\_ids=GROUP\_IDS,
    since=SINCE,
    until=UNTIL
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search for. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | A comma-separated list of group fields you want included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-group) for descriptions of all available fields. |
| `GROUP_IDS`  <br>_Optional_ | List | A comma-separated list of Meta Content Library group IDs as strings. Limits the query to groups in the list. Maximum of 250 IDs. |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook groups created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the group.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook groups created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the group.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |