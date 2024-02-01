platform: TikTok
topic: Example
subtopic: Developer Terms
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Example/Developer Terms.md
url: https://developers.tiktok.com/doc/research-api-specs-query-videos/

## Example

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/video/query/?fields=id,video_description,create_time' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "query": {
            "and": [
                {
                    "operation": "IN",
                    "field_name": "region_code",
                    "field_values": ["JP", "US"]
                },
                {
                    "operation":"EQ",
                    "field_name":"hashtag_name",
                    "field_values":["animal"]
                }
            ],
            "not": [
              {
                    "operation": "EQ",
                    "field_name": "video_length",
                    "field_values": ["SHORT"]
               }
            ]
        },
        "max_count": 100,
        "cursor": 0,
        "start_date": "20230101",
        "end_date": "20230115"
    }'