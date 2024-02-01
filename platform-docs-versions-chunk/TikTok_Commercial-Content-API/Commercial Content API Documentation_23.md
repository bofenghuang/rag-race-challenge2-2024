platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-details/

## Request example

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/detail/?fields=ad.id,ad.first_shown_date,ad.last_shown_date' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json'
    --data-raw '{
       "ad_id": 104836593772645
    }'
    

# Response

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Example** |
| data | AdDetailData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |