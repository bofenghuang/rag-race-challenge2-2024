platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities


## Tweet with an animated GIF

Below is the extended entities metadata for this Tweet with an animated GIF:

> Test Tweet with animated GIF [pic.twitter.com/nD6G4bWSKb](https://t.co/nD6G4bWSKb)
> 
> — @FloodSocial demo (@FloodSocial) [May 31, 2017](https://twitter.com/FloodSocial/status/870042717589340160)

    {
      "extended_entities": {
        "media": [
          {
            "id": 870042654213459968,
            "id_str": "870042654213459968",
            "indices": [
              29,
              52
            ],
            "media_url": "http://pbs.twimg.com/tweet_video_thumb/DBMDLy_U0AAqUWP.jpg",
            "media_url_https": "https://pbs.twimg.com/tweet_video_thumb/DBMDLy_U0AAqUWP.jpg",
            "url": "https://t.co/nD6G4bWSKb",
            "display_url": "pic.twitter.com/nD6G4bWSKb",
            "expanded_url": "https://twitter.com/FloodSocial/status/870042717589340160/photo/1",
            "type": "animated_gif",
            "sizes": {
              "medium": {
                "w": 350,
                "h": 262,
                "resize": "fit"
              },
              "small": {
                "w": 340,
                "h": 255,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "large": {
                "w": 350,
                "h": 262,
                "resize": "fit"
              }
            },
            "video_info": {
              "aspect_ratio": [
                175,
                131
              ],
              "variants": [
                {
                  "bitrate": 0,
                  "content_type": "video/mp4",
                  "url": "https://video.twimg.com/tweet_video/DBMDLy_U0AAqUWP.mp4"
                }
              ]
            }
          }
        ]
      }
    }