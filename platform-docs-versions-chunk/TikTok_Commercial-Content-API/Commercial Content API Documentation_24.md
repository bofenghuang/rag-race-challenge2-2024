platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-get-ad-details/


## Response example

    {
       "data": {
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
                "unique_users_seen": "30K",
                "unique_users_seen_by_country": {
                   "GB": "18K",
                   "IT": "12K"
                }
             },
             "rejection_info": {
                 "affected_countries": ["FR", "IT"] 
             }
          },
          "ad_group": {
             "target" {
                "number_of_users_targeted": "50K",
                "country": ["IT", "GB"],
                "age": {
                   "13-17": false,
                   "18-24": false,
                   "25-34": false,
                   "35-44": true,
                   "35-44": true,
                   "55+": true,
                },
                "gender": {
                   "female": true,
                   "male": true,
                   "other_genders": true
                },
                "audience_targeting": "No",
                "video_interactions": "Entertainment",
                "creator_interactions": "Talent",
                "interest": "News & Entertainment, Business Services"
             }
          },
          "advertiser": {
              "business_id": 1755645247067185,
              "business_name": "Awesome Co.",
              "country_code": "US",
              "paid_by": "Awesome Co.",
              "tiktok_account": {
                "avatar_url": "https://asdf.tiktokcdn.com/1736254.jpeg?x-expires=1679169600\u0026x-signature=asdf",
                "follower_count": 26374,
                "profile_url": "https://www.tiktok.com/@awesome_co"
              }
          }
       },
       "error": {
          "code": "ok",
          "http_status_code": 200,
          "log_id": "202207280326050102231031430C7E754E",
          "message": ""
       }
    }