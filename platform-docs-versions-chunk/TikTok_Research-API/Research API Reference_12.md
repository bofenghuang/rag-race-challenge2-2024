platform: TikTok
topic: Research-API
subtopic: Research API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Reference.md
url: https://developers.tiktok.com/doc/research-api-specs-query-video-comments/

# Query Video Comments

# Request

|     |     |
| --- | --- |
| **HTTP** **URL** | https://open.tiktokapis.com/v2/research/video/comment/list/ |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example Value** |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |
| Content-Type | string | Content type for the return data | application/json |

## Query Parameters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | The requested fields. Choose from the Comment Object fields. | **Complete list**:<br><br>id, video\_id, text, like\_count, reply\_count, parent\_comment\_id, create\_time | Yes |