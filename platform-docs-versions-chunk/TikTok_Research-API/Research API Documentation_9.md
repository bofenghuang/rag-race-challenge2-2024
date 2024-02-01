platform: TikTok
topic: Research-API
subtopic: Research API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Documentation.md
url: https://developers.tiktok.com/doc/research-api-get-started/


### Next page

With the cURL command below, you can get the next page of query results.

    curl -X POST \
      'https://open.tiktokapis.com/v2/research/video/query/?fields=id,like_count' \
      -H 'authorization: bearer clt.example12345Example12345Example' \
      -d '{ 
              "query": {
                  "and": [
                       { "operation": "IN", "field_name": "region_code", "field_values": ["US", "IN"] },
                       { "operation": "GT", "field_name": "hashtag_name", "field_values": ["hello"] }
                   ]
              }, 
              "max_count": 10,
              "cursor": 10,
              "start_date": "20220615",
              "end_date": "20220628",
              "search_id": "7160776277492814854",
    }'
    

The following example data is returned from the response.

    {
        "data": {
            "cursor": 20,
            "has_more": true,
            "search_id": "7160776277492814854",
            "videos": [
                ...
            ]
        },
        "error": {
            ...
        } 
    }