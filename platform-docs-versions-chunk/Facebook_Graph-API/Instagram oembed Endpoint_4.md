platform: Facebook
topic: Graph-API
subtopic: Instagram oembed Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Instagram oembed Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/instagram-oembed/


### Fields

| Field | Description |
| --- | --- |
| `author_name`<br><br>string | The name of the Instagram user that owns the post.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `html`<br><br>string | The HTML used to display the post.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `provider_name`<br><br>string | Name of the provider (Instagram)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `provider_url`<br><br>string | URL of the provider (Instagram)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `thumbnail_height`<br><br>int32 | The height of the thumbnail.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `thumbnail_url`<br><br>string | A url for the post's raw image asset. It must respect the 'maxwidth' parameter from the request. Prefer using the HTML field instead. However, you may use this field if loading the embed code is not an option. If you embed an Instagram image this way, you must provide clear attribution next to the image, including attribution to the original author and to Instagram, and a link to the Instagram media page.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `thumbnail_width`<br><br>int32 | The width of the thumbnail.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `type`<br><br>string | The oEmbed resource type. See https://oembed.com/.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `version`<br><br>string | Always 1.0. See https://oembed.com/<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `width`<br><br>int32 | The width in pixels required to display the HTML.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |