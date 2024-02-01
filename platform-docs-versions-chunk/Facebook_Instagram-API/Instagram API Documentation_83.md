platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Create a Tagged Container for Reels

Use the [IG User Media](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media) endpoint to create a media container for Reels. Alternatively, see [Create Tagged Media Container](#post-media) or [Carousels](#carousels).

POST /{ig\-user\-id}/media

#### Parameters

* `media_type` — You must specify the media type `REELS`.
* `video_url` — The path to the video for the Reel. Your video must be on a public server. Your video must meet the [Reels Specifications](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#reel-specifications).
* `thumb_offset` — The location, in milliseconds, of the frame for the video's cover thumbnail image. The default value is `0`, which is the first frame of the video.
* `caption` — The caption for the Reel.
* `product_tags` — (**required**) An array of objects specifying the product tags to add to the Reel. You can specify up to 30 tags, and the tags and product IDs must be unique. Tags for out-of-stock products are supported. Each object should have the following information:  
    * `product_id` — (**required**) Product ID.
* `location_id` — The ID of a Page associated with a location that you want to tag the video with. For details, see [IG User Media Query String Parameters](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#query-string-parameters).
* `share_to_feed` — `true` to request that the video appears on both the Feed and Reels tabs. `false` to request that the video appears only on the Reels tab.
* `access_token` — Your [User Access Token](https://developers.facebook.com/docs/facebook-login/guides/access-tokens).

If the operation is successful the API returns a container ID which you can use to [publish the container](#post-media-publish).

#### Sample Request

curl \-i \-X POST \\
 "https://graph.facebook.com/`v19.0`/90010177253934/media?media\_type=REELS&video\_url=https://upl...&product\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3231775643511089'%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/v12.0/90010177253934/media?media\_type=REELS&video\_url=https://upl...
&product\_tags=\[
  {
    product\_id:'3231775643511089'
  }
\]&access\_token=EAAOc...

#### Sample Response

{
  "id": "17969578066508312"
}

[](#)