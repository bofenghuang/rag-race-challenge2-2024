platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media


### Fields

Public fields can be read via field expansion.

FieldDescription

`caption`  
Public

Caption. Excludes album children. The `@` symbol is excluded, unless the app user can perform admin-equivalent [tasks](https://developers.facebook.com/docs/pages/overview#tasks) on the Facebook Page connected to the Instagram account used to create the caption.

`comments_count`  
Public

Count of comments on the media. Excludes comments on album child media and the media's caption. Includes replies on comments.

`copyright_check_information.status`

Returns `status` and `matches_found` objects

| status objects | Description |
| --- | --- |
| `status` | * `completed` – the detection process has finished<br>* `error` – an error occurred during the detection process<br>* `in_progress` – the detection process is ongoing<br>* `not_started` – the detection process has not started |
| `matches_found` | Set to one of the following:<br><br>* `false` if the video **does not violate** copyright,<br>* `true` if the video **does violate** copyright |

If a video **is violating copyright**, the `copyright_matches` is returned with an array of objects about the copyrighted material, when the violation is occurring in the video, and the actions take to mitigate the violation.

| copyright\_matches objects | Description |
| --- | --- |
| `author` | the author of the copyrighted video |
| `content_title` | the name of the copyrighted video |
| `matched_segments` | An array of objects with the following key-value pairs: \* `duration_in_seconds` – the number of seconds the content violates copyright \* `segment_type` – either `AUDIO` or `VIDEO` \* `start_time_in_seconds` – set to the start time of the video |
| `owner_copyright_policy` | Objects returned include:<br><br>* `name` – The name for the copyright owners' policy<br>* `actions` – An array of `action` objects with the mitigations steps taken defined by the copyright owner's policy. May include different mitigations steps for different locations.<br>    <br>    * `action` – The mitigation action taken against the video violating copyright. Different mitigation steps can be taken for different countries. Can be one of the following values:<br>        * `BLOCK` – The video is blocked from the audiences listed in the `geos` array<br>        * `MUTE` - The video is muted for audiences listed in the `geos` array |

`id`  
Public

Media ID.

`ig_id`  
Public

Instagram media ID. Used with Legacy Instagram API, now deprecated. Use `id` instead.

`is_comment_enabled`

Indicates if comments are enabled or disabled. Excludes album children.

`is_shared_to_feed`  
Public

For Reels only. When `true`, indicates that the reel can appear in both the **Feed** and **Reels** tabs. When `false`, indicates that the reel can only appear in the **Reels** tab.

Neither value determines whether the reel actually appears in the **Reels** tab because the reel may not meet eligibilty requirements or may not be selected by our algorithm. See [reel specifications](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#reel-specifications) for eligibility critera.

`like_count`

Count of likes on the media, including replies on comments. Excludes likes on album child media and likes on promoted posts created from the media.

  

If queried indirectly through another endpoint or field expansion:

  

* **v10.0 and older calls:** The value is `0` if the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts.
* **v11.0+ calls:** The `like_count` field is omitted if the media owner has hidden like counts.

`media_product_type`  
Public

Surface where the media is published. Can be `AD`, `FEED`, `STORY` or `REELS`.

`media_type`  
Public

Media type. Can be `CAROUSEL_ALBUM`, `IMAGE`, or `VIDEO`.

`media_url`  
Public

The URL for the media.

The `media_url` field is omitted from responses if the media contains copyrighted material or has been flagged for a copyright violation. Examples of copyrighted material can include audio on reels.

`owner`  
Public

Instagram user ID who created the media. Only returned if the app user making the query also created the media; otherwise, `username` field is returned instead.

`permalink`  
Public

Permanent URL to the media.

`shortcode`  
Public

Shortcode to the media.

`thumbnail_url`  
Public

Media thumbnail URL. Only available on `VIDEO` media.

`timestamp`  
Public

[ISO 8601](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FISO_8601&h=AT36Cl0BbNKBPwepFRBeBL9J6FTH_HA7EaK6B_c5l5IGjQo9WGuJuzXZJbfKkkUcNVDqVONtOKnzM0dZdEGj7cvj6ZU5oqjlznTqyqa8624uGQaj8oP6r9zhVChjco-lppq0MmqK-tNVS-BL)\-formatted creation date in UTC (default is UTC ±00:00).

`username`  
Public

Username of user who created the media.

`video_title`  
Public

Deprecated. Omitted from response.