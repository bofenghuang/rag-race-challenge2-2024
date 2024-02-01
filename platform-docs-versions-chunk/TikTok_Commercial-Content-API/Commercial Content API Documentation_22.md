platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-details/

## Query parameters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | The requested fields:<br><br>* ad.id<br>* ad.first\_shown\_date<br>* ad.last\_shown\_date<br>* ad.status<br>* ad.status\_statement<br>* ad.videos<br>* ad.image\_urls<br>* ad.reach<br>* advertiser.business\_id<br>* advertiser.business\_name<br>* advertiser.paid\_for\_by<br>* advertiser.follower\_count<br>* advertiser.avatar\_url<br>* advertiser.profile\_url<br>* ad\_group.targeting\_info | ad.id,ad.first\_shown\_date,ad.last\_shown\_date | true |

## Body

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| ad\_id | i64 | The ad ID. | 104836593772645 | false |