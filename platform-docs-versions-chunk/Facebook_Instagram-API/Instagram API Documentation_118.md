platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/changelog

## May 26, 2021

If indirectly querying an IG Media through another endpoint, the [like\_count](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will now return `0` if the app user does not [own](https://developers.facebook.com/docs/instagram-api/overview#authorization) the media and the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts on it. Directly querying the IG Media, which can only be done by the IG Media owner, will return the actual like count, even if the owner has hidden like counts on the media.

[](#)

## May 4, 2021

Made a minor change to how we calculate the [`online_followers`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights#metrics-and-periods) metric on IG Users.

[](#)