platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-ads/

## Request example

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad.id,ad.first_shown_date,ad.last_shown_date' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json' \
    --data-raw '{
       "filters":{
           "advertiser_business_ids": [3847236290405, 319282903829],
           "ad_published_date_range": {
                "min": "20210102",
                "max": "20210109"
           },
           "country_code": "FR",
           "unique_users_seen_size_range": {
               "min": "10K",
               "max": "1M"
           },
       },
       "search_term": "mobile games"
    }'
    

# Response

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Example** |
| data | QueryAdData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |