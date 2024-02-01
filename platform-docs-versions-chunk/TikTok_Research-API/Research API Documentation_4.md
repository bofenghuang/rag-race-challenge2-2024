platform: TikTok
topic: Research-API
subtopic: Research API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Documentation.md
url: https://developers.tiktok.com/doc/research-api-get-started/

# Query TikTok public content data

The cURL command below shows an example of how you can query the TikTok ID and like count of videos created in the US or Canada with the keyword `hello world` in the video description.

     
    curl -X POST \
      'https://open.tiktokapis.com/v2/research/video/query/?fields=id,like_count' \
      -H 'authorization: bearer clt.example12345Example12345Example' \
      -d '{ 
              "query": {
                  "and": [
                       { "operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"] },
                       { "operation": "EQ", "field_name": "keyword", "field_values": ["hello world"] }
                   ]
              }, 
              "start_date": "20220615",
              "end_date": "20220628",
              "max_count": 10
    }'