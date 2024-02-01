platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/content-publishing


## Reels Posts

Reels are short-form videos that are eligible to appear in the **Reels** tab of the Instagram app if they meet certain [specifications](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#reel-specifications) and are selected by our algorithm. To publish a reel, follow the steps for publishing a [single media post](#single-media-posts) and include the `media_type=REELS` parameter along with the path to the video using the `video_url` parameter.

Reels are not a new media type, even though you set `media_type=REELS` when you publish a reel. If you publish a reel and then request its `media_type` field, the value returned is `VIDEO`. To determine if a published video has been designated as a reel, request its `media_product_type` field instead.

You can use the [code sample on GitHub (insta\_reels\_publishing\_api\_sample)](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffbsamples%2Freels_publishing_apis%2Ftree%2Fmain%2Finsta_reels_publishing_api_sample&h=AT3EZ6hzCKzB-Edyukmi5cAVtNo9vcpnHXzDjk1leIAIzZIFeaavQAQyB9jo9lwS2teLBVQlU6hXfBovH4gcwnKLCevDWfLDHtDG7H1NbPZf-nzynViLXQ1NXXzFdh7jAGxw7oxSp1xRt5Ge6B-6HQ) to learn how to publish Reels to Instagram.

To make it more convenient for developers, Meta has published the full set of Graph API calls for Instagram Reels on the Postman API Platform. For more information, see [Postman Collections for Facebook Reels and Instagram Reels](https://developers.facebook.com/docs/reels/postman).

For more information about Reels, see [Reels Developer Documentation](https://developers.facebook.com/docs/reels).

[](#)