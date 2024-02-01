platform: TikTok
topic: Research-API
subtopic: Research API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Reference.md
url: https://developers.tiktok.com/doc/research-api-specs-query-user-info/

# Query User Info

# Request

|     |     |
| --- | --- |
| **HTTP** **URL** | https://open.tiktokapis.com/v2/research/user/info/ |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example Value** |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Query Parameters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | Field names for desired data to be returned. It is a comma separated list.<br><br>See User Info Object below for a full list of values. | **Complete list**:<br><br>display\_name, bio\_description, avatar\_url, is\_verified, follower\_count, following\_count, likes\_count, video\_count | Yes |