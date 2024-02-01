platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_comment


### Field Expansion

You can expand the `media` field with a list of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) fields to get additional data on the IG Media entity on which the comment was made. For example:

media{id,media\_url}

**v10.0 and older calls until September 7, 2021:** The [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field on an IG Media will return `0` if the media [owner](https://developers.facebook.com/docs/instagram-api/overview#authorization) has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) through another endpoint or field expansion, the [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

#### Sample Field Expansion Request

curl -X GET \\
  'https://graph.facebook.com/`v19.0`/17841405309211844?fields=mentioned\_comment.comment\_id(17873440459141021){timestamp,like\_count,text,media{id,media\_url}}&access\_token=IGQVJ...'

#### Sample Field Expansion Response

{
  "mentioned\_comment": {
    "timestamp": "2017-05-03T16:09:08+0000",
    "like\_count": 185,
    "text": "Shout out to @metricsaurus",
    "id": "17873440459141021",
    "media": {
      "id": "17895695668004550",
      "media\_url": "https://scont..."
    }
  },
  "id": "17841405309211844"
}