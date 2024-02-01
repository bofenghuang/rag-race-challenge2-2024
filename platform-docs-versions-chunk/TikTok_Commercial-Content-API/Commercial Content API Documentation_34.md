platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-report/

### DateRange

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| min | string | The first date of the range.<br><br>"min" needs to be after October 1st, 2022. | 20230102 | true |
| max | string | The last date of the range. | 20230109 | true |

## Request example

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/report/?fields=count_time_series_by_country' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json'
    --data-raw '{
       "filters":{
           "ad_published_date_range": {
                "min": "20230102",
                "max": "20230109"
           },
           "country_code":"ALL",
           "advertiser_business_ids":[21836478203048,3484763562784]
       }
    }'