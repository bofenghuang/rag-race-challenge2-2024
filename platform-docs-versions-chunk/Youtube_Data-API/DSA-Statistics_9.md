platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### CommentThreads

A `**commentThread**` resource contains information about a YouTube comment thread, which comprises a top-level comment and replies, if any exist, to that comment. A `commentThread` resource can represent comments about either a video or a channel.  
  
Both the top-level comment and the replies are actually `[comment](https://developers.google.com/youtube/v3/docs/comments)` resources nested inside the `commentThread` resource. The `commentThread` resource does not necessarily contain all replies to a comment, and you need to use the `[comments.list](https://developers.google.com/youtube/v3/docs/comments/list)` method if you want to retrieve all replies for a particular comment. Also note that some comments do not have replies.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/commentThreads#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/commentThreads#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[list](https://developers.google.com/youtube/v3/docs/commentThreads/list)` | `GET /commentThreads` | Returns a list of comment threads that match the API request parameters. |
| `[insert](https://developers.google.com/youtube/v3/docs/commentThreads/insert)` | `POST /commentThreads` | Creates a new top-level comment. To add a reply to an existing comment, use the `[comments.insert](https://developers.google.com/youtube/v3/docs/comments/insert)` method instead. |