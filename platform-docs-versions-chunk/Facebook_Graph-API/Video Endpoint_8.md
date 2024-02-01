platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/comments/

### Parameters

| Parameter | Description |
| --- | --- |
| `filter`<br><br>enum{stream, toplevel} | Default value: `toplevel`<br><br>SELF\_EXPLANATORY |
| `live_filter`<br><br>enum{filter\_low\_quality, no\_filter} | Default value: `filter_low_quality`<br><br>For comments on a Live streaming video, this determines whether low quality comments will be filtered out of the results (filtering is enabled by default). In all other circumstances this parameter is ignored. |
| `order`<br><br>enum{chronological, reverse\_chronological} | Preferred ordering of the comments. Accepts chronological (oldest first) and reverse chronological (newest first). If the comments can be ranked, then the order will always be ranked regardless of this modifier. The best practice for querying comments on a Live video is to continually poll for comments in the reversechronological ordering mode. |
| `since`<br><br>datetime | Lower bound of the time range to consider |