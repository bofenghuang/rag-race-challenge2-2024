platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/entities


### Media size objects

All Tweets with native media (photos, video, and GIFs) will include a set of ‘thumb’, ‘small’, ‘medium’, and ‘large’ sizes with height and width pixel sizes.  For photos and preview image media URLs, [Photo Media URL formatting](#photo_format) specifies how to construct different URLs for loading different sized photo media.

#### Sizes object 

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| thumb | [Size Object](#size) | Information for a thumbnail-sized version of the media. Example:<br><br>"thumb":{"h":150, "resize":"crop", "w":150}<br><br>Thumbnail-sized photo media will be limited to _fill_ a 150x150 boundary and cropped. |
| large | [Size Object](#size) | Information for a large-sized version of the media. Example:<br><br>"large":{"h":1366, "resize":"fit", "w":2048}<br><br>Large-sized photo media will be limited to fit within a 2048x2048 boundary. |
| medium | [Size Object](#size) | Information for a medium-sized version of the media. Example:<br><br>"medium":{"h":800, "resize":"fit", "w":1200}<br><br>Medium-sized photo media will be limited to _fit_ within a 1200x1200 boundary. |
| small | [Size Object](#size) | Information for a small-sized version of the media. Example:<br><br>"small":{"h":454, "resize":"fit", "w":680}<br><br>Small-sized photo media will be limited to fit within a 680x680 boundary. |

#### Size object 

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| w   | Int | Width in pixels of this size. Example:<br><br>"w":150 |
| h   | Int | Height in pixels of this size. Example:<br><br>"h":150 |
| resize | String | Resizing method used to obtain this size. A value of _fit_ means that the media was resized to fit one dimension, keeping its native aspect ratio. A value of _crop_ means that the media was cropped in order to fit a specific resolution. Example:<br><br>"resize":"crop" |