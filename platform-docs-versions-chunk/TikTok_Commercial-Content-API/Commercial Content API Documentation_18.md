platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-advertisers/

## Request example

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/advertiser/query/?fields=business_id,business_name' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json'
    --data-raw '{
       "search_term": "awesome",
       "max_count": 25
    }'
    

# Response

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Example** |
| data | QueryAdvertiserData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |