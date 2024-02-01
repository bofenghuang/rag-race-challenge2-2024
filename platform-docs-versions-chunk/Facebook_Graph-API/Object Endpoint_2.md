platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/comments


# `/{object-id}/comments`

This reference describes the `/comments` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `/comments` edge:

|     |     |     |
| --- | --- | --- |
| * [Album](https://developers.facebook.com/docs/graph-api/reference/album/)<br>    <br>* [Comment](https://developers.facebook.com/docs/graph-api/reference/comment/)<br>    <br>* [Event](https://developers.facebook.com/docs/graph-api/reference/event/)<br>    <br>* [Link](https://developers.facebook.com/docs/graph-api/reference/link/) | * [Live Video](https://developers.facebook.com/docs/graph-api/reference/live-video/)<br>    <br>* [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/)<br>    <br>* [Post](https://developers.facebook.com/docs/graph-api/reference/post/) | * [Thread](https://developers.facebook.com/docs/graph-api/reference/thread/)<br>    <br>* [User](https://developers.facebook.com/docs/graph-api/reference/user/)<br>    <br>* [Video](https://developers.facebook.com/docs/graph-api/reference/video/) |

It is possible for comment objects to have a `/comments` edge, which is called _comment replies_. The structure is the same for these, but attention should be paid to the [modifiers](#readmodifiers) for these edges.