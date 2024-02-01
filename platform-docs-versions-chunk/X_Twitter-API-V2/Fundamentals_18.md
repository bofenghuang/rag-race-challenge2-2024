platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media


## Media

Media refers to any image, GIF, or video attached to a Tweet. The media object is not a primary object on any endpoint, but can be found and expanded in the Tweet object. 

The object is available for expansion with `?expansions=attachments.media_keys` to get the condensed object with only default fields. Use the expansion with the field parameter: `media.fields` when requesting additional fields to complete the object.

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| media\_key (default) | string | Unique identifier of the expanded media content.<br><br>`"media_key": "13_1263145212760805376"` | Can be used to programmatically retrieve media |
| type (default) | string | Type of content (animated\_gif, photo, video).<br><br>`"type": "video"` | Classify the media as a photo, GIF, or video |
| url | string | A direct URL to the media file on Twitter. | Returns a Media object with a URL field for photos |
| duration\_ms | integer | Available when type is video. Duration in milliseconds of the video.<br><br>`"duration_ms": 46947` |     |
| height | integer | Height of this content in pixels.<br><br>`"height": 1080` |     |
| non\_public\_metrics | object | Non-public engagement metrics for the media content at the time of the request. <br><br>Requires user context authentication.<br><br>`"non_public_metrics": {            "playback_0_count": 1561,            "playback_100_count": 116,            "playback_25_count": 559,            "playback_50_count": 305,            "playback_75_count": 183,          }` | Determine video engagement: how many users played through to each quarter of the video. |
| organic\_metrics | object | Engagement metrics for the media content, tracked in an organic context, at the time of the request. <br><br>Requires user context authentication.<br><br>`"organic_metrics": {            "playback_0_count": 1561,            "playback_100_count": 116,            "playback_25_count": 559,            "playback_50_count": 305,            "playback_75_count": 183,            "view_count": 629          }` | Determine organic media engagement. |
| preview\_image\_url | string | URL to the static placeholder preview of this content.<br><br>`"preview_image_url": "https://pbs.twimg.com/media/EYeX7akWsAIP1_1.jpg"` |     |
| promoted\_metrics | object | Engagement metrics for the media content, tracked in a promoted context, at the time of the request. <br><br>Requires user context authentication.<br><br>`"promoted_metrics": {            "playback_0_count": 259,            "playback_100_count": 15,            "playback_25_count": 113,            "playback_50_count": 57,            "playback_75_count": 25,            "view_count": 124          }` | Determine media engagement when the Tweet was promoted. |
| public\_metrics | object | Public engagement metrics for the media content at the time of the request.<br><br>`"public_metrics": {            "view_count": 6865141          }` | Determine total number of views for the video attached to the Tweet. |
| width | integer | Width of this content in pixels.<br><br>`"width": 1920` |     |
| alt\_text | string | A description of an image to enable and support accessibility. Can be up to 1000 characters long. Alt text can only be added to images at the moment. <br><br>"alt\_text": “Rugged hills along the Na Pali coast on the island of Kauai” | Can be used to provide a written description of an image in case a user is visually impaired. |
| variants | array | Each media object may have multiple display or playback variants, with different resolutions or formats<br><br>`"variants": [`<br><br>  `{        "bit_rate": 632000,        "content_type":"video/mp4",        "url": "https://video.twimg.com/ext_tw_video/1527322141724532740/pu/vid/320x568/lnBaR2hCqE-R_90a.mp4?tag=12"       }`<br><br> `]` |     |