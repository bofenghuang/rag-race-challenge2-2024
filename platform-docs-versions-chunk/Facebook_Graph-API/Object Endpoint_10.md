platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/comments


### Fields

| Name | Description |
| --- | --- |
| `attachment_id`<br><br>_string_ | An optional ID of a unpublished photo (see `no_story` field in [`/{user-id}/photos`](https://developers.facebook.com/docs/graph-api/reference/user/photos/#publish)) uploaded to Facebook to include as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `attachment_share_url`<br><br>_string_ | The URL of a GIF to include as a animated GIF comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `attachment_url`<br><br>_string_ | The URL of an image to include as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `source`<br><br>_[multipart/form-data](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml401%2Finteract%2Fforms.html%23h-17.13.4.2&h=AT14LZC5hjWe8bL-LKxW4Qhyj1eE3a7b6gXW1K-kfFJDFU86ccgah0hT2DLdLVJWJIMnwTPipTGSMscIHmbBWOKA1LmYbto7Vund8pfmMq2kuJwbVEbZV4bUW95YZwCXXwerk_ZSWkJD862c)_ | A photo, encoded as form data, to use as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `message`<br><br>_string_ | The comment text. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing.<br><br>Mention other Facebook Pages in your `message` text using the following syntax:<br><br>`@[page-id]`<br><br>Usage of [this feature is subject to review](https://developers.facebook.com/docs/apps/review/feature#reference-MENTIONING). |