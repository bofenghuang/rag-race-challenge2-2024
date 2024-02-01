platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-details/

### AdVideo

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| url | string | The video url of this ad. | https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime\_type=video\_mp4 |

### Reach

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| unique\_users\_seen | string | The total number of unique users who have seen this ad. | 10K |
| unique\_users\_seen\_by\_country | map<string,string> | The total number of unique users who have seen this ad in each country. | {<br><br>"GB": "13K",<br><br>"IT": "12K"<br><br>} |