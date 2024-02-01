platform: Facebook
topic: Graph-API
subtopic: Instagram oembed Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Instagram oembed Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/instagram-oembed/

### Parameters

| Parameter | Description |
| --- | --- |
| `hidecaption`<br><br>boolean | If set to true, the embed code hides the caption. Defaults to false if parameter is not included in request. |
| `maxwidth`<br><br>int64 | Maximum width of returned media. Must be between 320 and 658. Note that the maxheight parameter is not supported. This is because the embed code is responsive and its height varies depending on its width and length of the caption. |
| `omitscript`<br><br>boolean | If set to true, the returned embed HTML code will not include any javascript. |
| `url`<br><br>URI | The post's URL.<br><br>Required |