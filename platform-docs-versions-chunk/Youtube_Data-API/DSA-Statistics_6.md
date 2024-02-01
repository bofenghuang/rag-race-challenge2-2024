platform: Youtube
topic: Data-API
subtopic: DSA-Statistics
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Youtube_Data-API/DSA-Statistics.md
url: https://developers.google.com/youtube/v3/docs


### ChannelBanners

A `channelBanner` resource contains the URL that you would use to set a newly uploaded image as the banner image for a channel.

For more information about this resource, see its [resource representation](https://developers.google.com/youtube/v3/docs/channelBanners#resource) and list of [properties](https://developers.google.com/youtube/v3/docs/channelBanners#properties).

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |     |     |
| `[insert](https://developers.google.com/youtube/v3/docs/channelBanners/insert)` | `POST /channelBanners/insert` | Uploads a channel banner image to YouTube. This method represents the first two steps in a three-step process to update the banner image for a channel:<br><br>1. Call the `channelBanners.insert` method to upload the binary image data to YouTube. The image must have a 16:9 aspect ratio and be at least 2048x1152 pixels. We recommend uploading a 2560px by 1440px image.<br>2. Extract the `url` property's value from the response that the API returns for step 1.<br>3. Call the `[channels.update](https://developers.google.com/youtube/v3/docs/channels/update)` method to update the channel's branding settings. Set the `[brandingSettings.image.bannerExternalUrl](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.image.bannerExternalUrl)` property's value to the URL obtained in step 2. |