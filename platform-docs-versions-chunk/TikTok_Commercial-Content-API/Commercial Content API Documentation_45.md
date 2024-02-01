platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-commercial-content/

### CommercialContent

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| id  | i64 | The commercial content ID. | 38267490502373 |
| create\_date | string | The create date of the commercial content in format of YYYYMMDD. | 20230109 |
| create\_timestamp | i64 | The create date of the commercial content in format of Unix timestamp. | 1696875852 |
| label | string | The label of this commercial content. | Paid partnership |
| brand\_names | list<string> | The brands that sponsor this commercial content. | \[<br><br>"My Awesome Co.",<br><br>"HelloWorld Inc."<br><br>\] |
| creator | CommercialContentCreator | The commercial content creator's public information. |     |
| video | CommercialContentVideo | The commercial content video's public information. |     |