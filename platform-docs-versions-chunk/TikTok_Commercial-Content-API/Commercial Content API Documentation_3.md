platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-getting-started/

## Pagination

If the total number of ads that match the search criteria is larger than the maximum number of ads that can be returned in a single request, the response data will be returned with different requests.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Field** | **Type** | **Description** | **Example** | **Required?** |
| max\_count | number | The maximum count of TikTok videos in the response. The default value is 10 and the maximum value is 50. | 12  | FALSE |
| search\_id | string | The ID of a previous search to provide sequential calls for paging. | "eyJsYXN0X3NvcnQiOls3NDA3OCwiMzUwNDIwOTgzOD" | FALSE |