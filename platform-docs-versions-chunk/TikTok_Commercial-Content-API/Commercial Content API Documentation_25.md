platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-details/

## Data structures

### GetAdDetailData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| advertiser | Advertiser | The advertiser metadata. |     |
| ad\_group | AdGroup | The ad group metadata. |     |
| ad  | Ad  | The ad metadata. |     |

### Advertiser

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| business\_id | i64 | The advertiser's business ID. | 1755645247067185 |
| business\_name | string | The advertiser's business name. | Awesome Co. |
| country\_code | string | The advertiser's country in the format of a two-letter code defined in ISO 3166-1. | US  |
| paid\_by | string | The advertiser's funding source. | Awesome Co. |
| tiktok\_account | TikTokAccount | The advertiser's TikTok account information. | See example in TikTokAccount table |