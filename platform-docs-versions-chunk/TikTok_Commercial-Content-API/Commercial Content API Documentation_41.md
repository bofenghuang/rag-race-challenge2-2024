platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-commercial-content/

### DateRange

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| min | string | The first date of the range and this needs to be after October 1st, 2022. | 20230102 | true |
| max | string | The last date of the range. | 20230109 | true |

## Request example

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/commercial_content/report/?fields=ad_id,video_urls,business_name' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json' \
    --data-raw '{
       "filters":{
           "content_published_date_range": {
                "min": "20210102",
                "max": "20210109"
           },
           "creator_country_code": "FR"
       }
     }'