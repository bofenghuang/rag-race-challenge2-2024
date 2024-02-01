platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/entities


### Media object  

The `entities` section will contain a `media` array containing a single media object if any media object has been ‘attached’ to the Tweet. If no native media has been attached, there will be no `media` array in the `entities`. For the following reasons the `extended_entities` section should be used to process Tweet native media:  
\+ Media `type` will always indicate ‘photo’ even in cases of a video and GIF being attached to Tweet.  
\+ Even though up to four photos can be attached, only the first one will be listed in the `entities` section.

The `has:media` Operator will match if this array is populated.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| display\_url | String | URL of the media to display to clients. Example:<br><br>"display\_url":"pic.twitter.com/rJC5Pxsu" |
| expanded\_url | String | An expanded version of display\_url. Links to the media display page. Example:<br><br>"expanded\_url": "http://twitter.com/yunorno/status/114080493036773378/photo/1" |
| id  | Int64 | ID of the media expressed as a 64-bit integer. Example:<br><br>"id":114080493040967680 |
| id\_str | String | ID of the media expressed as a string. Example:<br><br>"id\_str":"114080493040967680" |
| indices | Array of Int | An array of integers indicating the offsets within the Tweet text where the URL begins and ends. The first integer represents the location of the first character of the URL in the Tweet text. The second integer represents the location of the first non-URL character occurring after the URL (or the end of the string if the URL is the last part of the Tweet text). Example:<br><br>"indices":\[15,35\] |
| media\_url | String | An http:// URL pointing directly to the uploaded media file. Example:<br><br>"media\_url":"http://pbs.twimg.com/media/DOhM30VVwAEpIHq.jpg"<br><br>For media in direct messages, `media_url` is the same https URL as `media_url_https` and must be accessed by signing a request with the user’s access token using OAuth 1.0A.<br><br>It is not possible to access images via an authenticated twitter.com session. Please visit [this page](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/retrieving-media) to learn how to account for these recent change. <br><br>You cannot directly embed these images in a web page.<br><br>See [Photo Media URL formatting](#photo_format) for how to format a photo's URL, such as `media_url_https`, based on the available `sizes`. |
| media\_url\_https | String | An https:// URL pointing directly to the uploaded media file, for embedding on https pages. Example:<br><br>"media\_url\_https":"https://p.twimg.com/AZVLmp-CIAAbkyy.jpg"<br><br>For media in direct messages, `media_url_https` must be accessed by signing a request with the user’s access token using OAuth 1.0A.<br><br>It is not possible to access images via an authenticated twitter.com session. Please visit [this page](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/retrieving-media) to learn how to account for these recent change. <br><br>You cannot directly embed these images in a web page.<br><br>See [Photo Media URL formatting](#photo_format) for how to format a photo's URL, such as `media_url_https`, based on the available `sizes`. |
| sizes | [Size Object](#size) | An object showing available sizes for the media file. Example:<br><br>{<br>  "sizes": {<br>    "thumb": {<br>      "h": 150,<br>      "resize": "crop",<br>      "w": 150<br>    },<br>    "large": {<br>      "h": 1366,<br>      "resize": "fit",<br>      "w": 2048<br>    },<br>    "medium": {<br>      "h": 800,<br>      "resize": "fit",<br>      "w": 1200<br>    },<br>    "small": {<br>      "h": 454,<br>      "resize": "fit",<br>      "w": 680<br>    }<br>  }<br>}<br><br>See [Photo Media URL formatting](#photo_format) for how to format a photo's URL, such as `media_url_https`, based on the available `sizes`. |
| source\_status\_id | Int64 | Nullable. For Tweets containing media that was originally associated with a different tweet, this ID points to the original Tweet. Example:<br><br>"source\_status\_id": 205282515685081088 |
| source\_status\_id\_str | Int64 | Nullable. For Tweets containing media that was originally associated with a different tweet, this string-based ID points to the original Tweet. Example:<br><br>"source\_status\_id\_str": "205282515685081088" |
| type | String | Type of uploaded media. Possible types include photo, video, and animated\_gif. Example:<br><br>"type":"photo" |
| url | String | Wrapped URL for the media link. This corresponds with the URL embedded directly into the raw Tweet text, and the values for the `indices` parameter. Example:<br><br>"url":"http://t.co/rJC5Pxsu" |