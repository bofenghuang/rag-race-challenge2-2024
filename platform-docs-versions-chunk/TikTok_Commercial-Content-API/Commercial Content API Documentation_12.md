platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-query-ads/


## Response example

    {
       "data": {
          "ads": [
             {
                "ad": {
                   "first_shown_date": 20210101,
                   "id": 1923845247192304,
                   "image_urls": [
                      "https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf"
                   ],
                   "last_shown_date": 20210101,
                   "status": "active",
                   "videos": [
                      {"url": "https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime_type=video_mp4"},
                      {"url": "https://asdfcdn.com/..../1kmeidhfb38u21nd82hsk389fd/?mime_type=video_mp4"}
                   ],
                   "reach": {
                      "unique_user_seen": "11K"
                    }
                },
                "advertiser": {
                    "buisness_id": 3847236290405,
                    "business_name": "Awe Food Co.",
                    "paid_by": "Awe Co."
                }
             }
          ],
          "has_more": "true",
          "search_id": "2837438294054038"
       },
       "error": {
          "code": "ok",
          "http_status_code": 200,
          "log_id": "202304280326050102231031430C7E754E",
          "message": ""
       }
    }