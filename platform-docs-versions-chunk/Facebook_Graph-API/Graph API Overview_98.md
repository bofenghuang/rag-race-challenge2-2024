platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/field-expansion


## Nested Requests

The field expansion feature of the Graph API allows you to effectively nest multiple graph queries into a single call. For example, in a single call, you can ask for the first N photos of the first K albums. The response maintains the data hierarchy so developers do not have to weave the data together on the client. This is different from the [batch requests](https://developers.facebook.com/docs/graph-api/making-multiple-requests/) feature which allows you to make multiple, potentially unrelated, Graph API calls in a single request.

Here is the general format that field expansion takes:

GET graph.facebook.com/{node-id}?fields=LEVEL-ONE{LEVEL-TWO}

`LEVEL-ONE` in this case would be one or more (comma-separated) fields or edges from the parent node. `LEVEL-TWO` would be one or more (comma-separated) fields or edges from the first level node.

There is no limitation to the amount of nesting of levels that can occur here. You can also use a `.limit(n)` argument on each field or edge to restrict how many objects you want to get.

This is easier to understand by seeing it in action, so here's an example query that will retrieve up to five posts your published, with the text from each individual post.

GET graph.facebook.com/me?fields=posts.limit(5){message}

We can then extend this a bit more and for each post object, we get the text and privacy setting of each post. By default the `privacy` field returns an object that contains information about five key:value pairs, `allow`, `deny`, `description`, `friends`, and `value`. In this query we only want one returned, the `value` key:value pair.

GET graph.facebook.com/me?fields=posts.limit(5){message,privacy{value}}

Now we can extend it again by retrieving the name of each photo, the picture URL, and the people tagged:

GET graph.facebook.com
  /me?fields=albums.limit(5){name, photos.limit(2){name, picture, tags.limit(2)}},posts.limit(5)

Let's look at an example using cursor-based pagination:

GET graph.facebook.com
  /me?fields=albums.limit(5){name,photos.limit(2).after(MTAyMTE1OTQwNDc2MDAxNDkZD){name,picture,tags.limit(2)}},posts.limit(5)

You can see how field expansion can work across nodes, edges, and fields to return really complex data in a single request.

#### Limitations

* Certain resources, including most of Marketing API, are unable to utilize field expansion on some or all connections.