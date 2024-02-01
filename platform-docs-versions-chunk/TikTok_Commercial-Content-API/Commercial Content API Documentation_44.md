platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-commercial-content/

## Data structures

### QueryCommercialContentData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| commercial\_contents | list<CommercialContent> | The list of commercial contents. |     |
| has\_more | bool | The flag that indicates if there are more items to be returned. | true |
| search\_id | string | A search\_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria.<br><br>If you update the`filters` in the request, please remove the `search_id` to avoid getting back unexpected results | "eyJsYXN0X3NvcnQiOlsyNTQxMTkwLCIzNDk1NzA4NjI0N" |