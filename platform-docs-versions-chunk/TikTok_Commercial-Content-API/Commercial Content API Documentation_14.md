platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-ads/

### Ad

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| id  | i64 | The ad ID. | 1923845247192304 |
| first\_shown\_date | string | The first day when this ad was shown. | 20210101 |
| last\_shown\_date | string | The last day when this ad was shown. | 20210101 |
| status | string | The audit status of this ad: active or inactive. | active |
| videos | list<AdVideo> | The list of videos. |     |
| image\_urls | list<string> | The image URL list of this ad. | \[<br><br>"https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\\u0026x-signature=asdf"<br><br>\] |
| reach | Reach | The number of users who have seen this ad. | {<br><br>"unique\_users\_seen": "11K"<br><br>} |

### AdVideo

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| url | string | The video url of this ad | https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime\_type=video\_mp4 |