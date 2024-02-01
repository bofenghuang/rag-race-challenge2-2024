platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-commercial-content/

# Query Commercial Content

Use POST /v2/research/adlib/commercial\_content/query/ to query commercial content

|     |     |
| --- | --- |
| **HTTP URL** | https://open.tiktokapis.com/v2/research/adlib/commercial\_content/query/ |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

# Request

## Headers

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | The original media type of the resource. | application/json | true |