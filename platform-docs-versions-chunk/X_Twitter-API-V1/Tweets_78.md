platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update_with_media


### Example Request[¶](#example-request "Permalink to this headline")

**Note:** The example request here demonstrates the multipart request format.

POST /1.1/statuses/update\_with\_media.json HTTP/1.1
Host: api.twitter.com
User-Agent: Go http package
Content-Length: 15532
Authorization: OAuth oauth\_consumer\_key="...", oauth\_nonce="...", oauth\_signature="...", oauth\_signature\_method="HMAC-SHA1", oauth\_timestamp="1347058301", oauth\_token="...", oauth\_version="1.0"
Content-Type: multipart/form-data;boundary=cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340
Accept-Encoding: gzip

--cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340
Content-Disposition: form-data; name="status" Hello 2012-09-07 15:51:41.375247 -0700 PDT!
--cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340

Content-Type: application/octet-stream
Content-Disposition: form-data; name="media\[\]"; filename="media.png" ...
--cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340-- 

{
  "contributors": null,
  "coordinates": null,
  "created\_at": "Fri Sep 07 22:46:18 +0000 2012",
  "entities": {
    "hashtags": \[\],
    "media": \[
      {
        "display\_url": "pic.twitter.com/lX5LVZO",
        "expanded\_url": "https://twitter.com/fakekurrik/status/244204973972410368/photo/1",
        "id": 244204973989187584,
        "id\_str": "244204973989187584",
        "indices": \[
          44,
          63
        \],
        "media\_url": "http://pbs.twimg.com/media/A2OXIUcCUAAXj9k.png",
        "media\_url\_https": "https://pbs.twimg.com/media/A2OXIUcCUAAXj9k.png",
        "sizes": {
          "large": {
            "h": 175,
            "resize": "fit",
            "w": 333
          },
          "medium": {
            "h": 175,
            "resize": "fit",
            "w": 333
          },
          "small": {
            "h": 175,
            "resize": "fit",
            "w": 333
          },
          "thumb": {
            "h": 150,
            "resize": "crop",
            "w": 150
          }
        },
        "type": "photo",
        "url": "http://t.co/lX5LVZO"
      }
    \],
    "urls": \[\],
    "user\_mentions": \[\]
  },
  "favorited": false,
  "geo": null,
  "id": 244204973972410368,
  "id\_str": "244204973972410368",
  "in\_reply\_to\_screen\_name": null,
  "in\_reply\_to\_status\_id": null,
  "in\_reply\_to\_status\_id\_str": null,
  "in\_reply\_to\_user\_id": null,
  "in\_reply\_to\_user\_id\_str": null,
  "place": null,
  "possibly\_sensitive": false,
  "retweet\_count": 0,
  "retweeted": false,
  "source": "Fakekurrik's Test Application",
  "text": "Hello 2012-09-07 15:48:27.889593 -0700 PDT! http://t.co/lX5LVZO",
  "truncated": false,
  "user": {
    "contributors\_enabled": false,
    "created\_at": "Fri Sep 09 16:13:20 +0000 2011",
    "default\_profile": false,
    "default\_profile\_image": false,
    "description": "I am just a testing account, following me probably won't gain you very much",
    "entities": {
      "description": {
        "urls": \[\]
      },
      "url": {
        "urls": \[
          {
            "display\_url": null,
            "expanded\_url": null,
            "indices": \[
              0,
              24
            \],
            "url": "http://blog.roomanna.com"
          }
        \]
      }
    },
    "favourites\_count": 1,
    "follow\_request\_sent": false,
    "followers\_count": 2,
    "following": false,
    "friends\_count": 5,
    "geo\_enabled": true,
    "id": 370773112,
    "id\_str": "370773112",
    "is\_translator": false,
    "lang": "en",
    "listed\_count": 0,
    "location": "Trapped in factory",
    "name": "fakekurrik",
    "notifications": false,
    "profile\_background\_color": "C0DEED",
    "profile\_background\_image\_url": "http://a0.twimg.com/profile\_background\_images/616512781/iarz5lvj7lg7zpg3zv8j.jpeg",
    "profile\_background\_image\_url\_https": "https://si0.twimg.com/profile\_background\_images/616512781/iarz5lvj7lg7zpg3zv8j.jpeg",
    "profile\_background\_tile": true,
    "profile\_image\_url": "http://a0.twimg.com/profile\_images/2440719659/x47xdzkguqxr1w1gg5un\_normal.png",
    "profile\_image\_url\_https": "https://si0.twimg.com/profile\_images/2440719659/x47xdzkguqxr1w1gg5un\_normal.png",
    "profile\_link\_color": "0084B4",
    "profile\_sidebar\_border\_color": "C0DEED",
    "profile\_sidebar\_fill\_color": "FFFFFF",
    "profile\_text\_color": "333333",
    "profile\_use\_background\_image": true,
    "protected": true,
    "screen\_name": "fakekurrik",
    "show\_all\_inline\_media": false,
    "statuses\_count": 546,
    "time\_zone": "Pacific Time (US & Canada)",
    "url": "http://blog.roomanna.com",
    "utc\_offset": -28800,
    "verified": false
  }
}