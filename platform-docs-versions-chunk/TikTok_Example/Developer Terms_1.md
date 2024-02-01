platform: TikTok
topic: Example
subtopic: Developer Terms
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Example/Developer Terms.md
url: https://developers.tiktok.com/doc/research-api-specs-query-videos/

# Query Videos

# Request

|     |     |
| --- | --- |
| **HTTP** **URL** | https://open.tiktokapis.com/v2/research/video/query/ |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| Content-Type | string | Indicate the original media type of the resource. | "application/json" | Yes |
| Authorization | string | The client access token which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | Yes |