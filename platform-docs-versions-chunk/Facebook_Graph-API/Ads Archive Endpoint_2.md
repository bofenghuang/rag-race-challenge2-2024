platform: Facebook
topic: Graph-API
subtopic: Ads Archive Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Ads Archive Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/ads_archive/

### Filters

You can use filters in your search query to return only certain types of ads. See `bylines` and `publisher_platforms` below.

### Examples

To return archived ads related to social issues, elections and politics that contain the word 'california' and reached an audience in the US:

cURL

    curl -G \
    -d "search_terms='california'" \
    -d "ad_type=POLITICAL_AND_ISSUE_ADS" \
    -d "ad_reached_countries=['US']" \
    -d "access_token=<ACCESS_TOKEN>" \
    "https://graph.facebook.com/<VERSION>/ads_archive"

  
Show Response