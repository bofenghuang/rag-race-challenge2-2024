platform: TikTok
topic: Research-API
subtopic: Research API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Reference.md
url: https://developers.tiktok.com/doc/research-api-specs-query-video-comments/


### Example

    {
        "data": {
            "comments": [
                {
                    "text": "AWEEEEEE 🥰🥰🥰",
                    "video_id": 1234563451201523412,
                    "create_time": 1671491598,
                    "id": 12345616934634134,
                    "like_count": 50,
                    "parent_comment_id": 1234561201524010,
                    "reply_count": 10
                },
                ...
            ],
            "has_more": true,
            "cursor": 300
        },
        "error": {
            "code": "ok",
            "message": "",
            "log_id": "202207280326050102231031430C7E754E"
        }
    }
    

  

**Personal information (phone number, email and credit card account, etc) in the comments will be redacted. See the example below.**

Comment (original): "Could you please contact me? 4059233930 is my number. Hi Edmond, email Mwen numerow at acharles@emortgagecapital.com, epi map relew. Download “Temu” make an account then search up 23216471 then click accept."

Comment (returned by the API): "Could you please contact me? 40\*\*\*\*\*\*30 is my number.

Hi Edmond, email Mwen numerow at a\*\*\*\*\*\*\*@\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*, epi map relew.

Download “Temu” make an account then search up \*\*\*\*6471 then click accept."