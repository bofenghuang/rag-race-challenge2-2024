platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-advertisers/

## Query parameters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | The requested fields:<br><br>* business\_name<br>* business\_id<br>* country\_code | business\_name,business\_id,country\_code | true |

## Body

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| search\_term | string | The terms to search for in the query. The limit of the string is 50 characters or less. | awesome | true |
| max\_count | i64 | The maximum number of results returned at once. The default value is 10 and the maximum value is 50. | 20  | false |