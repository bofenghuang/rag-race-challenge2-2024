platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-ads/

## Data structures

### RequestFilters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| ad\_published\_date\_range | DateRange | The date range during which the ads were published.<br><br>The "min" value should represent a date after October 1, 2022. | {<br><br>"min": 20230102,<br><br>"max": 20230109<br><br>} | true |
| country\_code | string | The country where the ads were targeted. The default value is ALL.<br><br>[Supported Countries](https://developers.tiktok.com/doc/commercial-content-api-supported-countries) | FR  | false |
| advertiser\_business\_ids | list<i64> | The advertiser's business ID of the ads.<br><br>If you provide "search\_term", this filter will be ignored. | \[294854736284058, 495736284058473\] | false |
| unique\_users\_seen\_size\_range | SizeRange | The range of the number of users who've seen the content of this ad. | {<br><br>"min": "10K",<br><br>"max": "20K"<br><br>} | false |