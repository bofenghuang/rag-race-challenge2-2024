platform: Facebook
topic: Graph-API
subtopic: Media fingerprint Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Media fingerprint Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/media-fingerprint/


### Parameters

| Parameter | Description |
| --- | --- |
| `metadata`<br><br>array | The fingerprint metadata, for example: metadata={'episode':'newEpisodeVal','season':'newSeasonVal'} |
| `album`<br><br>string | Album name of a songtrack. This is a required metadata field for SONGTRACK content type. |
| `artist`<br><br>string | Artist name of a songtrack. This is a required metadata field for SONGTRACK content type. |
| `episode`<br><br>string | Episode name of an episode. This is a required metadata field for EPISODE content type. |
| `season`<br><br>string | Season name of an episode. This is a required metadata field for EPISODE content type. |
| `description`<br><br>string | Description of fingerprint. This is a required metadata field for MOVIE and OTHER content type. |
| `source`<br><br>file | The source of the new fingerprint file to update. Example: @myDirectory/myFile.mp4.rdm |
| `title`<br><br>string | The title of the media content |
| `universal_content_id`<br><br>string | A unique code user can use to manage fingerprint. For example: International Standard Recording Code for songtracks. This is for your own use; Facebook will not use this data. |