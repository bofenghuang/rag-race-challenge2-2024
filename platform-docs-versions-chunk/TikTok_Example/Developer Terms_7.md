platform: TikTok
topic: Example
subtopic: Developer Terms
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Example/Developer Terms.md
url: https://developers.tiktok.com/doc/research-api-specs-query-videos/

## Example

    {
        "data": {
            "videos": [
                {
                    "hashtag_names": [
                        "avengers",
                        "pov"
                    ],
                    "region_code": "CA",
                    "create_time": 1633823999,
                    "effect_ids": [
                        "0"
                    ],
                    "video_id": 702874395068494965,
                    "music_id": 703847506349838790,
                    "video_description": "lol #pov #avengers",
                    "view_count": 1050,
                    "comment_count": 2
                },
                ...
            ],
            "cursor": 100,
            "search_id": "7201388525814961198",
            "has_more": true
        },
        "error": {
            "code": "ok",
            "message": "",
            "log_id": "20230113024658F0D7C5D6CA3A9B79C5B9"
        }
    }