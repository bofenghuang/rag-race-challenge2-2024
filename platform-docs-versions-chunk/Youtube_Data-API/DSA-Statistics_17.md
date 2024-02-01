platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### Playlists

A `**playlist**` resource represents a YouTube playlist. A playlist is a collection of videos that can be viewed sequentially and shared with other users. A playlist can contain up to 200 videos, and YouTube does not limit the number of playlists that each user creates. By default, playlists are publicly visible to other users, but playlists can be public or private.  
  
YouTube also uses playlists to identify special collections of videos for a channel, such as:

* uploaded videos
* positively rated (liked) videos
* watch history
* watch later

To be more specific, these lists are associated with a channel, which is a collection of a person, group, or company's videos, playlists, and other YouTube information. You can retrieve the playlist IDs for each of these lists from the `[channel resource](https://developers.google.com/youtube/v3/docs/channels)` for a given channel.  
  
You can then use the `[playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list)` method to retrieve any of those lists. You can also add or remove items from those lists by calling the `[playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert)` and `[playlistItems.delete](https://developers.google.com/youtube/v3/docs/playlistItems/delete)` methods.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/playlists#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/playlists#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[delete](https://developers.google.com/youtube/v3/docs/playlists/delete)` | `DELETE /playlists` | Deletes a playlist. |
| `[list](https://developers.google.com/youtube/v3/docs/playlists/list)` | `GET /playlists` | Returns a collection of playlists that match the API request parameters. For example, you can retrieve all playlists that the authenticated user owns, or you can retrieve one or more playlists by their unique IDs. |
| `[insert](https://developers.google.com/youtube/v3/docs/playlists/insert)` | `POST /playlists` | Creates a playlist. |
| `[update](https://developers.google.com/youtube/v3/docs/playlists/update)` | `PUT /playlists` | Modifies a playlist. For example, you could change a playlist's title, description, or privacy status. |