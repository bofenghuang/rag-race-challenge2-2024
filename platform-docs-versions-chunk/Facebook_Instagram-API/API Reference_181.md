platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_media


### Fields

| Field | Description |
| --- | --- |
| `caption`  <br>_String_ | The caption text. Captions that @mention an IG User will not include the `@` symbol unless the app user created the IG Media object upon which the caption was made. |
| `comments`  <br>_Object_ | A list of IG Comments on the IG Media. If using Field Expansion to get the comment text, text that @mentions an IG User will not include the `@` symbol unless the app user created the IG Media object upon which the caption was made. |
| `comments_count`  <br>_String_ | Number of IG Comments on the IG Media. |
| `id`  <br>**Default**  <br>_String_ | ID of the IG Media. |
| `like_count`  <br>_String_ | Count of likes on the media. Excludes likes on album child media and likes on promoted posts created from the media. Includes replies on comments.<br><br>  <br><br>* **v10.0 and older calls:** value will be `0` if the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts it.<br>* **v11.0+ calls:** field will be omitted if media owner has hidden like counts in it Value will be `0` if the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts it. |
| `media_type`  <br>_String_ | The IG Media's type: `CAROUSEL_ALBUM`, `IMAGE`, `STORY`, or `VIDEO`. |
| `media_url`  <br>_String_ | URL of the published IG Media. |
| `owner`  <br>_String_ | ID of the IG User who created the IG Media. Only returned if the app user created the IG Media object, otherwise the `username` field will be returned instead. |
| `timestamp`  <br>_String_ | Creation date of IG Media formatted in ISO 8601. |
| `username`  <br>_String_ | Username of the IG User who created the IG Media. |