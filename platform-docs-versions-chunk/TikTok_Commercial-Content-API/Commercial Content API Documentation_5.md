platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-getting-started/

### Next page

With the cURL command below, you can get the next page of query results.

    curl -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad,ad_group' \
      -H 'authorization: bearer clt.example12345Example12345Example' \
      -d '{ 
              "filters": {
                  "ad_published_date_range": {
                     "min": "20221001",
                     "max": "20230510"
                  },
                  "country": "IT"
               }, 
              "search_term": "coffee",
              "max_count": 20,
              "search_id": "eyJsYXN0X3NvcnQiOls3NDA3OCwiMzUwNDIwOTgzOD"
           }'
    

The following example data is returned from the response.

    {
        "data": {
            "has_more": true,
            "search_id": "eyJsYXN0X3NvcnQiOlsyNTQxMTkwLCIzNDk1NzA4NjI",
            "ads": [
                ...
            ]
        },
        "error": {
            ...
        } 
    }