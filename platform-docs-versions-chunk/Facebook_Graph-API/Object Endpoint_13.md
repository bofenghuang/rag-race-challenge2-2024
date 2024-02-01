platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/likes

## Reading

Returns the list of people who liked this object. When reading likes on a Page or User object, this endpoint returns a list of pages liked by that Page or User.

Use the `likes` field of an object to get the number of likes.

We recommended that you use the [`/object/reactions` endpoint](https://developers.facebook.com/docs/graph-api/reference/object/reactions) to get like counts, if available.

### New Page Experience

The following objects `/likes` endpoint are supported for New Page Experience:

|     |     |
| --- | --- |
| * [Album](https://developers.facebook.com/docs/graph-api/reference/album)<br>* [Comment](https://developers.facebook.com/docs/graph-api/reference/comment)<br>* [Photo](https://developers.facebook.com/docs/graph-api/reference/photo)<br>* [PagePost](https://developers.facebook.com/docs/graph-api/reference/pagepost) | * User |

### Requirements

* The same requirements required to view the object are required to view likes on that object.