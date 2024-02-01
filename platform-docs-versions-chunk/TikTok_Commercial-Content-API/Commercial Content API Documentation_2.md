platform: TikTok
topic: Commercial-Content-API
subtopic: Commercial Content API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Commercial-Content-API/Commercial Content API Documentation.md
url: https://developers.tiktok.com/doc/commercial-content-api-getting-started/

# Obtain a client access token

Once you have obtained the client key and secret for your project, [generate a client access token](https://developers.tiktok.com/doc/client-access-token-management). Add this access token in the authorization header of the http requests to connect to the Commercial Content API endpoints.

# Query TikTok public content data

The cURL command below shows an example of how you can query the TikTok ads created in Italy between January 2, 2021 to January 9, 2021 with the keyword "coffee".

    curl -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad,ad_group' \
     -H 'authorization: bearer clt.example12345Example12345Example' \
     -d '{ 
             "filters": {
                "ad_published_date_range": {
                     "min": "20221001",
                     "max": "20230510"
                 },
                "country": "IT"
             }, 
            "search_term": "coffee",
            "max_count": 20
        }'