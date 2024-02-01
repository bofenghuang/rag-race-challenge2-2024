platform: TikTok
topic: Research-API
subtopic: Research API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Documentation.md
url: https://developers.tiktok.com/doc/research-api-get-started/


### First page

When you send the first request, you do not need to set the `search_id` or `cursor` in the request body. In the http response, `cursor` and `search_id` are returned, which are used in the subsequent requests.

    Try out this request:
    
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
              "start_date": "20220615",
              "end_date": "20220628",
              "max_count": 10
    }'
    

The following example data is returned from the response.

    {
        "data": {
            "cursor": 10,
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