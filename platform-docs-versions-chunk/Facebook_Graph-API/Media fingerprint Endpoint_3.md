platform: Facebook
topic: Graph-API
subtopic: Media fingerprint Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Media fingerprint Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/media-fingerprint/

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | Media fingerprint ID<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `duration_in_sec`<br><br>float | The length of the fingerprinted content, in seconds<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `fingerprint_content_type`<br><br>enum | Media fingerprint content type<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `metadata`<br><br>FingerprintMetadata | The metadata associated with the fingerprinted content |
| `title`<br><br>string | The title of the fingerprinted content |
| `universal_content_id`<br><br>string | A unique code user can use to manage fingerprint. For example: International Standard Recording Code for songtracks. This is for your own use; Facebook will not use this data. |