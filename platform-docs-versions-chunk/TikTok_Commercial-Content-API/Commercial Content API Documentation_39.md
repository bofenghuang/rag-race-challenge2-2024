platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-commercial-content/

## Body

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| filters | RequestFilters | Filters that will be applied to the query. | See the request example below | true |
| max\_count | i64 | The max number of results returned at once. The default value is 10, and the maximum value is 50. | 20  | false |
| search\_id | string | A search\_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. | "eyJsYXN0X3NvcnQiOlsyNTQxMTkwLCIzNDk1NzA4NjI0N" | false |

## Data structures