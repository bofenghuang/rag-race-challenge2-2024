platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### ChannelSections

A `**channelSection**` resource contains information about a set of videos that a channel has chosen to feature. For example, a section could feature a channel's latest uploads, most popular uploads, or videos from one or more playlists.  
  
Note that a channel's sections are only visible if the channel displays content in a browse view (rather than a feed view). To enable a channel to display content in a browse view, set the `[brandingSettings.channel.showBrowseView](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.channel.showBrowseView)` property to `true` for the specified channel.  
  
A channel can create a maximum of 10 shelves.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/channelSections#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/channelSections#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[delete](https://developers.google.com/youtube/v3/docs/channelSections/delete)` | `DELETE /channelSections` | Deletes a channel section. |
| `[insert](https://developers.google.com/youtube/v3/docs/channelSections/insert)` | `POST /channelSections` | Adds a channel section to the authenticated user's channel. A channel can create a maximum of 10 shelves. |
| `[list](https://developers.google.com/youtube/v3/docs/channelSections/list)` | `GET /channelSections` | Returns a list of `channelSection` resources that match the API request criteria. |
| `[update](https://developers.google.com/youtube/v3/docs/channelSections/update)` | `PUT /channelSections` | Updates a channel section. |