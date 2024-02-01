platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/content-publishing


## Carousel Posts

You may publish up to 10 images, videos, or a mix of the two in a single post (a carousel post). Publishing carousels is a three step process:

1. Use the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint to create individual item containers for each image and video that will appear in the carousel.
2. Use the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint again to create a single carousel container for the items.
3. Use the [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) endpoint to publish the carousel container.

Carousel posts count as a single post against the account's [rate limit](#rate-limit).

Limitations

* Carousels cannot be boosted.
* Carousels are limited to 10 images, videos, or a mix of the two.
* Carousel images are all cropped based on the first image in the carousel, with the default being a 1:1 aspect ratio.

Step 1 of 3: Create item container

Use the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint to create an item container for the image or video that will appear in a carousel. Carousels may have up to 10 total images, videos, or a mix of the two.

POST /{ig\-user\-id}/media

#### Parameters

The following parameters are **required**. Refer to the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint reference for additional supported parameters.

* `is_carousel_item` — Set to `true`. Indicates image or video will appear in a carousel.
* `image_url` — (images only) The path to the image. We will cURL your image using the passed in URL so it must be on a public server.
* `media_type` — (videos only) Set to `VIDEO`. Indicates media is a video.
* `video_url` — (videos only) Path to the video. We will cURL your video using the passed in URL so it must be on a public server.

If the operation is successful, the API will return an item container ID which can be used when creating the carousel container.

Repeat this process for each image or video that should appear in the carousel.

#### Sample Request

curl \-i \-X POST \\

"https://graph.facebook.com/`v19.0`/90010177253934/media?image\_url=https%3A%2F%2Fsol...&is\_carousel\_item=true&access\_token=EAAOc..."

#### Sample Response

{
  "id": "17899506308402767"
}

Step 2 of 3: Create carousel container

Use the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint to create a carousel container.

POST /{ig\-user\-id}/media

#### Parameters

The following parameters are **required**. Refer to the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint reference for additional supported parameters.

* `media_type` — Set to `CAROUSEL`. Indicates container is for a carousel.
* `children` — An array of up to 10 container IDs of each image and video that should appear in the published carousel. Carousels can have up to 10 total images, videos, or a mix of the two.

#### Sample Request

curl \-i \-X POST \\

"https://graph.facebook.com/`v19.0`/90010177253934/media?caption=Fruit%20candies&media\_type=CAROUSEL&children=17899506308402767%2C18193870522147812%2C17853844403701904&access\_token=EAAOc..."

#### Sample Response

{
  "id": "18000748627392977"
}

Step 3 of 3: Publish carousel container

Use the [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) endpoint to publish a carousel container (a carousel post). Accounts are limited to 50 published posts within a 24-hour period. Publishing a carousel counts as a single post.

POST /{ig\-user\-id}/media\_publish

#### Parameters

The following parameters are required.

* `creation_id` — The carousel container ID.

If the operation is successful the API will return a carousel album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) ID.

#### Sample Request

curl \-i \-X POST \\

"https://graph.facebook.com/`v19.0`/90010177253934/media\_publish?creation\_id=18000748627392977&access\_token=EAAOc..."

#### Sample Response

{
  "id": "90010778390276"
}

[](#)