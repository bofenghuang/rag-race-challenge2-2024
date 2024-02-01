platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/tags

### Edges

Use the `fields` query string parameter to specify Edges you want included on any returned [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media#read) objects.

### Response

A JSON-formatted object containing [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects.

{
  "{field}":"{value}",
  ...
}

### Pagination

This edge supports [cursor-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#paging) so the response will include `before` and `after` cursors if the response contains multiple pages of data. Unlike standard cursor-based pagination, however, the response will not include `previous` or `next` fields, so you will have to use the `before` and `after` cursors to construct `previous` and `next` query strings manually in order to page through the returned data set.

### Sample Request

GET graph.facebook.com/17841405822304914/tags
    ?fields=id,username
    &access\_token=EAADd...