platform: TikTok
topic: Research-API
subtopic: Research API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Documentation.md
url: https://developers.tiktok.com/doc/research-api-get-started/


# Query TikTok public account information

With the cURL command below, you can query public TikTok account information by a TikTok handle.

    curl --location --request POST 'https://open.tiktokapis.com/v2/research/user/info/?fields=display_name,bio_description,avatar_url,is_verified,follower_count,following_count,likes_count,video_count' \
    --header 'Authorization: bearer {{access_token}}' \
    --header 'Content-Type: text/plain' \
    --data-raw '{
        "username": "joe1234567"
    }'
    

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required?** |
| username | string | TikTok user's username | "Joe123" | FALSE |

  

The following example data is returned from the response.

    
    {
        "data": {
            "username": "joe1234567",
            "video_count": 64,
            "avatar_url": "https://my-awesome-avatar",
            "display_name": "joe 1234567",
            "follower_count": 111,
            "likes_count": 4146,
            "bio_description": "joe joe",
            "following_count": 103,
            "is_verified": false
        },
        "error": {
            ...
        }
    }