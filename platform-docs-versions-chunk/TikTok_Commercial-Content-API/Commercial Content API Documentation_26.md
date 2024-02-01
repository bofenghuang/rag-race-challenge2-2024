platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-details/

### TikTokAccount

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| profile\_url | string | The advertiser's TikTok profile link. | https://www.tiktok.com/@awesome\_co |
| avatar\_url | string | The advertiser's TikTok avatar link. | https://asdf.tiktokcdn.com/1736254.jpeg?x-expires=1679169600&x-signature=asdf |
| follower\_count | i64 | The advertiser's TikTok follower count. | 26374 |

### AdGroup

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| targeting\_info | TargetingInfo | The targeting of this ad group. | See example in Targeted table |