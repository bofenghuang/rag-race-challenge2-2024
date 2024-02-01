platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### Comments

A `**comment**` resource contains information about a single YouTube comment. A `comment` resource can represent a comment about either a video or a channel. In addition, the comment could be a top-level comment or a reply to a top-level comment.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/comments#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/comments#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[list](https://developers.google.com/youtube/v3/docs/comments/list)` | `GET /comments` | Returns a list of comments that match the API request parameters. |
| `[setModerationStatus](https://developers.google.com/youtube/v3/docs/comments/setModerationStatus)` | `POST /comments/setModerationStatus` | Sets the moderation status of one or more comments. The API request must be authorized by the owner of the channel or video associated with the comments. |
| `[insert](https://developers.google.com/youtube/v3/docs/comments/insert)` | `POST /comments` | Creates a reply to an existing comment. **Note:** To create a top-level comment, use the `[commentThreads.insert](https://developers.google.com/youtube/v3/docs/commentThreads/insert)` method. |
| `[markAsSpam](https://developers.google.com/youtube/v3/docs/comments/markAsSpam)` | `POST /comments/markAsSpam` | **Note:** This method has been deprecated and is no longer supported. |
| `[delete](https://developers.google.com/youtube/v3/docs/comments/delete)` | `DELETE /comments` | Deletes a comment. |
| `[update](https://developers.google.com/youtube/v3/docs/comments/update)` | `PUT /comments` | Modifies a comment. |