platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-ads/

### Reach

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| unique\_users\_seen | string | The number of users who have seen this ad. | "11K" |

### Advertiser

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| business\_id | i64 | The advertiser's business ID. | 1755645247067185 |
| business\_name | string | The advertiser's business name. | Awe Food Co. |
| paid\_by | string | The advertiser's funding source. | Awe Co. |

### ErrorStructV2

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| code | string | The error category in string. | ok  |
| message | string | The detailed error description. |     |
| log\_id | string | The unique ID associated with every request for debugging purporse. | 202207280326050102231031430C7E754E |
| http\_status\_code | i32 | The http status code. | 200 |