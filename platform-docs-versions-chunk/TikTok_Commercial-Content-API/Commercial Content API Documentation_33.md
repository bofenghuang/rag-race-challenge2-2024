platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-report/

## Body

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| filters | RequestFilters | Filters that will be applied to the query. | See the request example below. | true |

## Data structures

### RequestFilters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| ad\_published\_date\_range | DateRange | The time range when the ads were published.<br><br>"min" needs to be after October 1st, 2022. | {<br><br>"min": "20230102",<br><br>"max": "20230109"<br><br>} | true |
| country\_code | string | The country where the ads/ad groups were created. The default value is ALL.<br><br>[Supported Countries](https://developers.tiktok.com/doc/commercial-content-api-supported-countries) | FR  | false |
| advertiser\_business\_ids | list<i64> | The advertiser's business ID of the ads/ad groups. | \[21836478203048,3484763562784\] | false |