platform: Facebook
topic: Graph-API
subtopic: Album Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Album Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/album/


### Parameters

| Parameter | Description |
| --- | --- |
| `contributors`<br><br>list<int> | Contributors to turn this into a shared album |
| `description`<br><br>UTF-8 string | Deprecated. Use the message param<br><br>DeprecatedSupports Emoji |
| `is_default`<br><br>boolean | Default value: `false`<br><br>`true` indicates that the request will create the application specific album |
| `location`<br><br>string | A text location of the Album for non-page locations |
| `make_shared_album`<br><br>boolean | Default value: `false`<br><br>Ensures the created Album is a shared Album |
| `message`<br><br>string | The Album's caption. This appears below the title of the album in the Album view |
| `name`<br><br>UTF-8 string | The title of the Album<br><br>Supports Emoji |
| `place`<br><br>place tag | The ID of a location page to tag the Album with |
| `privacy`<br><br>Privacy Parameter | The privacy of the Album |
| `tags`<br><br>list<int> | Deprecated<br><br>Deprecated |
| `visible`<br><br>string | Deprecated. Use privacy<br><br>Deprecated |