platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag

### Edges

You can request the following edges as path parameters or by using the `fields` query string parameter.

| Edge | Description |
| --- | --- |
| [`recent_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/recent-media#reading) | Get a list of the most recently published photo and video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects published with a specific hashtag. |
| [`top_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/top-media#reading) | Returns the most popular photo and video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects that have been tagged with the hashtag. |

### Response

A JSON-formatted object containing default and requested [Fields](#fields).

{
  "{field}":"{value}",
  ...
}

### Sample Request

GET https://graph.facebook.com/17841593698074073
  ?fields=id,name
  &access\_token=EAADd...