platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-ads/

### DateRange

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| min | string | The first date of the range and this needs to be after October 1, 2022. | 20230102 | true |
| max | string | The last date of the range. | 20230109 | true |

### SizeRange

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| min | string | The minimum size in thousands (K), millions (M), or billions (B).<br><br>The number before "K", "M", and "B" must be an integer less than 1000. | Valid: 0K, 120K, 2M, 1B<br><br>Invalid: 2000K, 1.1M, 1B2M | false |
| max | string | The maximum size in thousands (K), millions (M), or billions (B)<br><br>The number before "K", "M", and "B" must be an integer less than 1000.<br><br>The value must be greater than 0. | Valid: 120K, 2M, 1B<br><br>Invalid: 0K, 2000K, 1.1M, 1B2M | false |