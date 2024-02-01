platform: Facebook
topic: Graph-API
subtopic: Comment Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Comment Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/comment


### Fields

| Property Name | Description | Type |
| --- | --- | --- |
| `id` | The comment ID | `string` |
| `attachment` | Link, video, sticker, or photo attached to the comment | [`StoryAttachment`](https://developers.facebook.com/docs/graph-api/reference/story-attachment/) |
| `can_comment` | Whether the viewer can reply to this comment | `bool` |
| `can_remove` | Whether the viewer can remove this comment | `bool` |
| `can_hide` | Whether the viewer can hide this comment. Only visible to a page admin | `boolean` |
| `can_like` | Whether the viewer can like this comment | `boolean` |
| `can_reply_privately` | Whether the viewer can send a private reply to this comment (Page viewers only) | `boolean` |
| `comment_count` | Number of replies to this comment | `int32` |
| `created_time` | The time this comment was made | `datetime` |
| `from` | The person that made this comment | [`User`](https://developers.facebook.com/docs/graph-api/reference/user/) |
| `like_count` | Number of times this comment was liked | `int32` |
| `message` | The comment text | `string` |
| `message_tags` | An array of Profiles tagged in `message`. | `object[]` |
| `id` | ID of the profile that was tagged. | `string` |
| `name` | The text used in the tag. | `string` |
| `type` | Indicates which type of profile is tagged. | `enum{user, page, group}` |
| `offset` | Where the first character of the tagged text is in the `message`, measured in [unicode code points](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCode_point&h=AT2Xq69VozGwNKTuVpXlrF76qrrNM8EDGa8l6pg6QYnd-rvWzPJLA6QUSvCom2SZLuBPKG4M7P7sJjqWTPUyFXyorn10Hcw5QBY-yN1_BKDnkEASamjmrf9AakfGRq3yy_OEnzRK9JXATaFe). | `integer` |
| `length` | How many [unicode code points](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCode_point&h=AT2pymolXehWtk3Jmb_66L6c1vmBIs9-wjCdHZBQTOxJ7BZ8vj8URu2kWjsGu26qG8TYijhIWzn2IDM6VXiAWx7VRxW9t0v5nPtNdQek7995w5lMNQ0TGQWhy-PzP-lVeFvFm9c_MttVvQb1) this tag consists of, after the offset. | `integer` |
| `object` | The comment on a post that contains a photo or video, including those in dynamic posts. Otherwise, this is empty. | `Object` |
| `parent` | For comment replies, this the comment that this is a reply to. | [`Comment`](https://developers.facebook.com/docs/graph-api/reference/comment) |
| `private_reply_conversation` | For comments with private replies, gets conversation between the Page and author of the comment (Page viewers only) | [`Conversation`](https://developers.facebook.com/docs/graph-api/reference/conversation) |
| `user_likes` | Whether the viewer has liked this comment. | `bool` |