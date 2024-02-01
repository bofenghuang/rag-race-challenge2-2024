platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/comments


### Fields

An array of [Comment objects](https://developers.facebook.com/docs/graph-api/reference/comment/) in addition to the following fields when `summary` is `true` in the request.

| Field | Description |
| --- | --- |
| `order`<br><br>_enum { chronological, reverse\_chronological }_ | Order in which comments were returned.<br><br>* `chronological`: Comments sorted by the oldest comments first.<br>* `reverse_chronological`: Comments sorted by the newest comments first. |
| `total_count`<br><br>_int32_ | The count of comments on this node. It is important to note that this value changes depending on the `filter` being used (where comment replies are available):<br><br>* if `filter` is `stream` then `total_count` will be a count of all comments (including replies) on the node.<br>* if `filter` is `toplevel` then `total_count` will be a count of all top-level comments on the node.<br><br>Note: `total_count` can be greater than or equal to the actual number of comments returned due to comment privacy or deletion. |