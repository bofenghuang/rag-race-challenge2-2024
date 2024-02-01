platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Create a Tagged Container for Images or Videos

Use the [IG User Media](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media) endpoint to create a media container for an [image](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#create-photo-container) or [video](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#create-video-container). Alternatively, see [Create Tagged Media Container for Reels](#post-media-reels) or [Carousels](#carousels).

POST /{ig\-user\-id}/media

#### Parameters

* `image_url` — (**required** for images only) The path to the image. Your image must be on a public server.
* `user_tags` — (images only) An array of public usernames and x/y coordinates for any public Instagram users who you want to tag in the image. The array must be formatted in JSON and contain a `username`, `x`, and `y` property. For example, `[{username:'natgeo',x:0.5,y:1.0}]`. `x` and `y` values must be floats that originate from the top-left of the image, with a range of `0.0`–`1.0`. Tagged users will receive a notification when the media is published.
* `video_url` — (**required** for videos only) The path to the video. Your video must be on a public server.
* `thumb_offset` — (videos only) The location, in milliseconds, of the frame for the video's cover thumbnail image. The default value is `0`, which is the first frame of the video.
* `product_tags` — (**required**) An array of objects specifying the product tags to add to the image or video. You can specify up to 20 tags for photo and video feed posts and up to 20 tags total per carousel post (up to 5 per carousel slide).
    * The tags and product IDs must be unique.
    * Tags for out-of-stock products are supported.
    * Each object should have the following information:  
        * `product_id` — (**required**) Product ID.
        * `x` — (images only) A float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.
    * `y` — (images only) A float that indicates percentage distance from top edge of the pu blished media image. Value must be within `0.0`–`1.0` range.

If the operation is successful the API returns a container ID which you can use to [publish the container](#post-media-publish).

#### Sample Request

curl \-i \-X POST \\
 "https://graph.facebook.com/`v19.0`/90010177253934/media?image\_url=https%3A%2F%2Fupl...&location\_id=7640348500&product\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3231775643511089'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/v12.0/90010177253934/media?image\_url=https://upl...&location\_id=7640348500
&product\_tags=\[
  {
    product\_id:'3231775643511089',
    x: 0.5,
    y: 0.8
  }
\]&access\_token=EAAOc...

#### Sample Response

{
  "id": "17969578066508312"
}

[](#)