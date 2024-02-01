platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/changelog


## June 8, 2021

#### Like Counts

_Applies to v11.0+. Will apply to all versions September 7, 2021._

If indirectly querying an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) through another endpoint or field expansion, the [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

  

#### Time-based Pagination

_Applies to v11.0+_.

Added [`since`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/#query-string-parameters) and [`until`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/#query-string-parameters) parameters to the [`GET /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/#reading) endpoint to support [time-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#time).

[](#)