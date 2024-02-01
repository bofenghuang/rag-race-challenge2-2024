platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media


### Limitations

#### General Limitations

* Containers expire after 24 hours.
* If the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted Instagram Professional account requires [Page Publishing Authorization](https://www.facebook.com/business/m/one-sheeters/page-publishing-authorization) (PPA), PPA must be completed or the request will fail.
* If the Page connected to the targeted Instagram Professional account requires two-factor authentication, the Facebook User must also have performed two-factor authentication or the request will fail.
* Publishing to Instagram TV is not supported.

#### Reels Limitations

* Reels cannot appear in album carousels.
* Account privacy settings are respected upon publish. For example, if **Allow remixing** is enabled, published reels will have remixing enabled upon publish but remixing can be disabled on published reels manually through the Instagram app.
* Music tagging is only available for original audio.

#### Story Limitations

* Stories expire after 24 hours.
* Support either video URL or Reels URL but not both.
* Publishing stickers (i.e., link, poll, location) is not supported.