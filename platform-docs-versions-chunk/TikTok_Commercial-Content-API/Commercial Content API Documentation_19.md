platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-advertisers/

## Response example

    {
       "data": {
          "advertisers": [
             {
                "business_id": 1755645247067185,
                "business_name": "Awesome Food Co.",
                "country_code": "US",        
             },
             {
                "business_id": 183746395837294,
                "business_name": "Awesome Drink Co.",
                "country_code": "CA",        
             }
          ]
       },
       "error": {
          "code": "ok",
          "http_status_code": 200,
          "log_id": "202207280326050102231031430C7E754E",
          "message": ""
       }
    }
    

## Data structures

### QueryAdvertiserData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| advertisers | list<Advertiser> | The list of advertisers that match all the criteria. |     |