platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-commercial-content/


## Response example

    {
       "data": {
          "commercial_contents": [
             {
                "brand_names": [
                   "My Awesome Co.",
                   "HelloWorld Inc."
                ],
                "create_date": "20230109",
                "create_timestamp": 1696875852,
                "creator": {
                   "username": "joe1234567"
                },
                "id": "v09044g40000ce6enu3c77u36l73sp20",
                "label": "Paid partnership",
                "videos": [
                   {
                      "cover_image_url": "https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf",
                      "url":"https://www.tiktok.com/@joe1234567/video/19384729204821234" 
                   }
                ]
             }
          ],
          "has_more": "true",
          "search_id": "2837438294054038"
       },
       "error": {
          "code": "ok",
          "http_status_code": 200,
          "log_id": "202207280326050102231031430C7E754E",
          "message": ""
       }
    }