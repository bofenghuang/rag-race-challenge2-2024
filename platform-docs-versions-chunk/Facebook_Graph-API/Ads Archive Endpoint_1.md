platform: Facebook
topic: Graph-API
subtopic: Ads Archive Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Ads Archive Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/ads_archive/

# Ad Library API

## Reading

Returns archived ads based on your search.

  

Reading with the API returns [archived ads](https://developers.facebook.com/docs/graph-api/reference/archived-ad/) from the [Meta Ad Library](https://www.facebook.com/ads/library) based on keyword searches of text, images, audio from video, and the call-to-action button. **Note that we do not translate your keyword searches**, therefore you should write them in the language of the ads you are searching. For example, if you are searching Spanish language ads you should write your search string in Spanish.

Learn more about the [Ad Library API](https://www.facebook.com/ads/library/api).

### End of Results

The ad objects are returned in `data`. If you paginate through results and reach a point where `data` contains no values, this means you have reached the end of the result set.

### Search by Page

You can request archived ads for up to 10 Facebook Page IDs at once by using the search parameter `search_page_ids`.