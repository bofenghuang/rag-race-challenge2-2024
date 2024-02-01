platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-commercial-content/

### RequestFilters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| content\_published\_date\_range | DateRange | The time range during which the commercial contents were published.<br><br>"min" needs to be after October 1st, 2022. | {<br><br>"min": 20230102,<br><br>"max": 20230109<br><br>} | true |
| creator\_country\_code | string | The country of the commercial content's author. The default value is ALL.<br><br>Supported countries: European Economic Area (EEA) countries [Supported Countries](https://developers.tiktok.com/doc/commercial-content-api-supported-countries)<br><br>Note: United Kingdom and Switzerland are not included in this API | FR  | false |
| creator\_usernames | list<string> | The commercial contents' creators. | \[<br><br>"joe123",<br><br>"emma\_lol"<br><br>\] | false |