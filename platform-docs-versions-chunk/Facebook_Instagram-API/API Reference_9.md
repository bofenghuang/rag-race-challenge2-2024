platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-comment


### Fields

| Field Name | Description |
| --- | --- |
| `from` | An object containing:<br><br>  <br><br>* `id` — [IGSID](https://developers.facebook.com/docs/messenger-platform/instagram/overview#igsid) of the Instagram user who created the IG Comment.<br>* `username` — Username of the Instagram user who created the IG Comment. |
| `hidden` | Indicates if comment has been hidden (`true`) or not (`false`). |
| `id` | IG Comment ID. |
| `like_count` | Number of likes on the IG Comment. |
| `media` | An object containing:<br><br>  <br><br>* `id` — ID of the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) upon which the IG Comment was made.<br>* `media_product_type` — Published surface of the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) (i.e. where the IG Media appears) upon which the IG Comment was made. |
| `parent_id` | ID of the parent IG Comment if this comment was created on another IG Comment (i.e. a reply to another comment. |
| `replies` | A list of replies (IG Comments) made on the IG Comment. |
| `text` | IG Comment text. |
| `timestamp` | ISO 8601 formatted timestamp indicating when IG Comment was created.<br><br>  <br><br>Example: `2017-05-19T23:27:28+0000`. |
| `user` | ID of IG User who created the IG Comment. Only returned if the app user created the IG Comment, otherwise `username` will be returned instead. |
| `username` | Username of Instagram user who created the IG Comment. |