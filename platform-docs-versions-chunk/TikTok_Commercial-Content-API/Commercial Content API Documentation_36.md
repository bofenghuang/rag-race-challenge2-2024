platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-report/

### DateCount

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| date | string | The date when ads were published in the format YYYYMMDD. | 20230101 |
| count | i64 | The total number of ads published on that date. | 500032 |

### ErrorStructV2

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| code | string | The error category in string. | ok  |
| message | string | The detailed error description. | ""  |
| log\_id | string | The unique ID associated with every request for debugging purposes. | 202207280326050102231031430C7E754E |
| http\_status\_code | i32 | The http status code. | 200 |