platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/search-quality


## Caveats and known limitations

#### Why would results be inconsistent from one time point to another?

Inconsistencies between identical searches made at separate time points can be caused by entity visibility changes over time, which may be due to content being created, deleted or modified. There may also occasionally be short lags between when content is created or modified and when it is indexed.

#### Why am I not seeing an entity I can find on the platform?

Apart from coverage gaps or delivery issues mentioned below (see [Factors affecting recall](#recallfactors)), it is possible the content is not eligible to be visible in the Meta Content Library and API. The visibility rules for content are complex and constantly evolving with new policies and regulations, making it possible that some content could be theoretically viewed by an individual on platform but not exposed via the Meta Content Library and API. For instance, visibility of some content is geographically restricted to users from the country where the content was produced. Also, direct mentions (via @) are not searchable, meaning that a result will not be returned if a matching term is only found in a direct mention.

#### Why would a search result not match my query?

Apart from tokenization issues listed below (see [Factors affecting precision](#precisionfactors)), it is possible that the content actually does contain the search terms, but they are found in different text fields or far apart within the text. Search matches query terms independently and scans all text fields visible from the UI. It also does not support phrase searching. Thus a search for “Walter Payton” could match a page listing basketball players “Walter Williams” and “Gary Payton” without reference to a “Walter Payton” anywhere in the text.