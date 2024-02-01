platform: TikTok
topic: Research-API
subtopic: Research API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Reference.md
url: https://developers.tiktok.com/doc/research-api-specs-query-video-comments/

### Body Parameters

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Required** |
| video\_id | int\_64 | The id of the video that the comments are made to. | Yes |
| max\_count | int64 | The number of comments in response.<br><br>Default is 10, max is 100.<br><br>It is possible that the API returns less comments than the max count due to reasons such as comments deleted by users etc. | No  |
| cursor | int64 | The starting index of the comments in the response.<br><br>**Note**: only the top 1000 comments will be returned, so cursor + max\_count <= 1000. | No  |

### Example

    curl -L POST 'https://open.tiktokapis.com/v2/research/video/comment/list/?fields=id,like_count,create_time,text,video_id,parent_comment_id' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type:application/json' \
    -d '{
      "video_id": 7178997441201524010,
      "max_count": 50,
      "cursor": 150
    }'
    

# Response