platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### Search

A search result contains information about a YouTube video, channel, or playlist that matches the search parameters specified in an API request. While a search result points to a uniquely identifiable resource, like a video, it does not have its own persistent data.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/search#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/search#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[list](https://developers.google.com/youtube/v3/docs/search/list)` | `GET /search` | Returns a collection of search results that match the query parameters specified in the API request. By default, a search result set identifies matching `[video](https://developers.google.com/youtube/v3/docs/videos)`, `[channel](https://developers.google.com/youtube/v3/docs/channels)`, and `[playlist](https://developers.google.com/youtube/v3/docs/playlists)` resources, but you can also configure queries to only retrieve a specific type of resource. |