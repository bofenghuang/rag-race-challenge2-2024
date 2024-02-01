platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### PlaylistItems

A `**playlistItem**` resource identifies another resource, such as a video, that is included in a playlist. In addition, the `playlistItem` resource contains details about the included resource that pertain specifically to how that resource is used in that playlist.  
  
YouTube also uses a playlist to identify a channel's list of uploaded videos, with each `playlistItem` in that list representing one uploaded video. You can retrieve the playlist ID for that list from the `[channel resource](https://developers.google.com/youtube/v3/docs/channels)` for a given channel. You can then use the `[playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list)` method to the list.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/playlistItems#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/playlistItems#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[delete](https://developers.google.com/youtube/v3/docs/playlistItems/delete)` | `DELETE /playlistItems` | Deletes a playlist item. |
| `[insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert)` | `POST /playlistItems` | Adds a resource to a playlist. |
| `[list](https://developers.google.com/youtube/v3/docs/playlistItems/list)` | `GET /playlistItems` | Returns a collection of playlist items that match the API request parameters. You can retrieve all of the playlist items in a specified playlist or retrieve one or more playlist items by their unique IDs. |
| `[update](https://developers.google.com/youtube/v3/docs/playlistItems/update)` | `PUT /playlistItems` | Modifies a playlist item. For example, you could update the item's position in the playlist. |