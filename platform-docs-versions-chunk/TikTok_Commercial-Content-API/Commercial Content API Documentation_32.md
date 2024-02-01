platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-report/

# Get Ad Report

Use POST /v2/research/adlib/ad/report/ to get a report on ad publishing.

|     |     |
| --- | --- |
| **HTTP** **URL** | https://open.tiktokapis.com/v2/research/adlib/ad/report/ |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

# Request

## Headers

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | Indicate the original media type of the resource. | application/json | true |

## Query parameters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | The requested fields:<br><br>* count\_time\_series\_by\_country | count\_time\_series\_by\_country | true |