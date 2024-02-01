platform: Facebook
topic: Graph-API
subtopic: Comment Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Comment Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/comment


### Fields

One of `attachment_url`, `attachment_id`, `message`, or `attachment_share_url` must be provided when updating.

You must include either a message or an attachment. An attachment can be either a `url`, an `attachment_id`, or an `attachment_share_url`. You may include an `id` and a `url` together. If you include an `attachment_share_url`, you must not include the others.

When updating you must include any values that were on the original content. If you do not include one of them it will be removed from the content after the update. For example, if you update a comment that has an image that was specified via `attachment_url` and you don't include it in the update the image will be removed.

Updating supports the fields listed on the [publishing section of the `/object/comments`](https://developers.facebook.com/docs/graph-api/reference/object/comments#publish). This includes the `attachment_url`, `attachment_id`, `message` and `source`. Please see that document for details on those fields.

Updating also supports the `is_hidden` field, documented here.

| Name | Description | Type |
| --- | --- | --- |
| `is_hidden` | Whether this comment is hidden or visible. The original poster can still see the comment, along with the page admin and anyone else tagged in the comment | `boolean` |