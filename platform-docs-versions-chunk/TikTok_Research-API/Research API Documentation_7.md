platform: TikTok
topic: Research-API
subtopic: Research API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Documentation.md
url: https://developers.tiktok.com/doc/research-api-get-started/

## Pagination

If the total number of videos that match the query criteria is larger than the max number of videos that can be returned in a single request, the response data will be returned with different requests.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Field** | **Type** | **Description** | **Example** | **Required?** |
| max\_count | number | The max count of TikTok videos in response. default: 10, max: 100 | 12  | FALSE |
| cursor | number | The starting index of TikTok videos in response. default: 0 | 100 | FALSE |
| search\_id | string | The ID of a previous search to provide sequential calls for paging | "7167072234702738478" | FALSE |