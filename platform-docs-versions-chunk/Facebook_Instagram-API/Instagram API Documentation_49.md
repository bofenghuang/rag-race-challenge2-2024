platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/content-publishing


## User Tags

You can tag public Instagram users in an image and they will receive a notification that they have been tagged.

To tag users in an image, follow the [Single Media Posts](#single-media-posts) steps above, but when creating the media container, include the `user_tags` parameter and an array of objects indicating the Instagram users in the image as well as their x/y coordinates within the image itself.

#### Sample Request

POST graph.facebook.com/17841400008460056/media
  ?image\_url=https://www.example.com/images/bronzed-fonzes.jpg
  &caption=#BronzedFonzes!
  &user\_tags=
   \[
     {
       username:'kevinhart4real',
       x: 0.5,
       y: 0.8
     },
     {
       username:'therock',
       x: 0.3,
       y: 0.2
     }
   \]

This returns a container ID which you then publish using the [IG User Media Publish](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) endpoint.

#### Notes

* The `user_tags` value must be an array of objects formatted with JSON.
* You can only tag users with public Instagram accounts.
* The object must contain all three properties (`username`, `x`, and `y`) for each user.
* `x` and `y` values must be `float` numbers that originate from the top-left of the image, with a range of `0.0`–`1.0`.
* User tags can be used with images in carousels.

[](#)