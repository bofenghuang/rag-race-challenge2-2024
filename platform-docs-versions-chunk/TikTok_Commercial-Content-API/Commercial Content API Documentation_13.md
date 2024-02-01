platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-ads/

## Data structures

### QueryAdData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| ads | list<AdDto> | The list of ads that match all the criteria. |     |
| has\_more | bool | The flag that indicates if there are more items to be returned. | true |
| search\_id | string | A unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. | 2837438294054038 |

### AdDto

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| ad  | Ad  | The metadata of this ad. |     |
| advertiser | Advertiser | The metadata of the advertiser. |     |