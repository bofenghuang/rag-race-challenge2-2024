platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/business_discovery

### Pagination

The `/media` edge supports [cursor-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#paging), so when accessing it via field expansion, the response will include `before` and `after` cursors if the response contains multiple pages of data. Unlike standard cursor-based pagination, however, the response will not include `previous` or `next` fields, so you will have to use the `before` and `after` cursors to construct `previous` and `next` query strings manually in order to page through the returned data set.

### Sample Request

GET graph.facebook.com
  /17841405309211844
    ?fields=business\_discovery.username(bluebottle){media{comments\_count,like\_count}}