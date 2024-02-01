platform: TikTok
topic: Research-API
subtopic: Research API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Reference.md
url: https://developers.tiktok.com/doc/research-api-specs-query-user-info/

### Body Parameters

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example Value** |
| username | string | username as the unique identifier | "joe11235" |

### Example

    curl -L 'https://open.tiktokapis.com/v2/research/user/info/?fields=display_name,bio_description,avatar_url,is_verified,follower_count,following_count,likes_count,video_count' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type:application/json' \
    -d '{"username": "joe123456"}'

# Response