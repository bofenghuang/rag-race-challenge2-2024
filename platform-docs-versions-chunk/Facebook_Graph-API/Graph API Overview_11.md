platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview

### Complex Parameters

Most parameter types are straightforward primitives such as `bool`, `string` and `int`, but there are also `list` and `object` types that can be specified in the request.

The `list` type is specified in JSON syntax, for example: `["firstitem", "seconditem", "thirditem"]`

The `object` type is also specified in JSON syntax, for example: `{"firstkey": "firstvalue", "secondKey": 123}`

## Publishing, Updating, and Deleting

Visit our [Facebook Sharing guide](https://developers.facebook.com/docs/sharing) to learn how to publish to a User's Facebook or our [Pages API documentation](https://developers.facebook.com/docs/pages) to publish to a Page's Facebook feed.

Some nodes allow you to update fields with `POST` operations. For example, you could update your `email` field like this:

curl -i -X POST \\
  "https://graph.facebook.com/USER-ID?email=YOURNEW@EMAILADDRESS.COM&access\_token=ACCESS-TOKEN"