platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-report/

# Response

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Example** |
| data | ReportData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

## Response example

    {
       "data": {
          "count_time_series_by_country": {
              "IT": [{"date": "20210109", "count": 45}, {"date": "20210108", "count": 24}],
              "ES": [{"date": "20210109", "count": 48}, {"date": "20210108", "count": 22}],
              ...
        }
       },
       "error": {
          "code": "ok",
          "http_status_code": 200,
          "log_id": "202207280326050102231031430C7E754E",
          "message": ""
       }
    }
    

## Data structures

### ReportData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| count\_time\_series\_by\_country | map<string,list<DateCount>> | The ad count time series of each country. |     |