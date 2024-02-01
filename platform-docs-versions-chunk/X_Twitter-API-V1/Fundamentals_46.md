platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/extended-entities


## Example Tweets and JSON payloads

Below are some example Tweets and their associated entities metadata.

Tweet with four native photos

Tweet with hashtag, user mention, cashtag, URL, and four native photos:

> Test Tweet with [@mentionThis](https://twitter.com/MentionThis) [$twtr](https://twitter.com/search?q=%24twtr&src=ctag) [https://t.co/RzmrQ6wAzD](https://t.co/RzmrQ6wAzD) [#hashtag](https://twitter.com/hashtag/hashtag?src=hash) [pic.twitter.com/9r69akA484](https://t.co/9r69akA484)
> 
> — @FloodSocial (@FloodSocial) [May 8, 2017](https://twitter.com/FloodSocial/status/861627479294746624)

Here is the `entities` section for this Tweet:

    {
      "entities": {
        "hashtags": [
          {
            "text": "hashtag",
            "indices": [
              59,
              67
            ]
          }
        ],
        "urls": [
          {
            "url": "https://t.co/RzmrQ6wAzD",
            "expanded_url": "http://bit.ly/2pUk4be",
            "display_url": "bit.ly/2pUk4be",
            "unwound": {
              "url": "https://blog.gnip.com/tweeting-in-the-rain/",
              "status": 200,
              "title": "Tweeting in the Rain, Part 1 - Gnip Blog - Social Data and Data Science Blog",
              "description": "If you would have told me a few years ago that one day I’d be comparing precipitation and social media time-series data, I would have assumed you were joking.  For 13 years at OneRain I helped develop software and monitoring … Continue reading →"
            },
            "indices": [
              35,
              58
            ]
          }
        ],
        "user_mentions": [
          {
            "screen_name": "MentionThis",
            "name": "Just Me",
            "id": 50247739,
            "id_str": "50247739",
            "indices": [
              16,
              28
            ]
          }
        ],
        "symbols": [
          {
            "text": "twtr",
            "indices": [
              29,
              34
            ]
          }
        ],
        "media": [
          {
            "id": 861627472244162561,
            "id_str": "861627472244162561",
            "indices": [
              68,
              91
            ],
            "media_url": "http://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
            "media_url_https": "https://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
            "url": "https://t.co/9r69akA484",
            "display_url": "pic.twitter.com/9r69akA484",
            "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
            "type": "photo",
            "sizes": {
              "medium": {
                "w": 1200,
                "h": 900,
                "resize": "fit"
              },
              "small": {
                "w": 680,
                "h": 510,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "large": {
                "w": 2048,
                "h": 1536,
                "resize": "fit"
              }
            }
          }
        ]
      }
    }

Only in this ‘extended’ payload below will you find the four (maximum) native photos. Notice that the first photo in the array is the same as the single photo included in the non-extended Twitter _entities_ section. The _media_ metadata structure for photos is the same for both _entities_ and _extended\_entities_ sections.

Here is the `extented_entities` section for this Tweet:

    {
    "extended_entities": {
        "media": [
          {
            "id": 861627472244162561,
            "id_str": "861627472244162561",
            "indices": [
              68,
              91
            ],
            "media_url": "http://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
            "media_url_https": "https://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
            "url": "https://t.co/9r69akA484",
            "display_url": "pic.twitter.com/9r69akA484",
            "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
            "type": "photo",
            "sizes": {
              "medium": {
                "w": 1200,
                "h": 900,
                "resize": "fit"
              },
              "small": {
                "w": 680,
                "h": 510,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "large": {
                "w": 2048,
                "h": 1536,
                "resize": "fit"
              }
            }
          },
          {
            "id": 861627472244203520,
            "id_str": "861627472244203520",
            "indices": [
              68,
              91
            ],
            "media_url": "http://pbs.twimg.com/media/C_UdnvPVYAAZbEs.jpg",
            "media_url_https": "https://pbs.twimg.com/media/C_UdnvPVYAAZbEs.jpg",
            "url": "https://t.co/9r69akA484",
            "display_url": "pic.twitter.com/9r69akA484",
            "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
            "type": "photo",
            "sizes": {
              "small": {
                "w": 680,
                "h": 680,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "medium": {
                "w": 1200,
                "h": 1200,
                "resize": "fit"
              },
              "large": {
                "w": 2048,
                "h": 2048,
                "resize": "fit"
              }
            }
          },
          {
            "id": 861627474144149504,
            "id_str": "861627474144149504",
            "indices": [
              68,
              91
            ],
            "media_url": "http://pbs.twimg.com/media/C_Udn2UUQAADZIS.jpg",
            "media_url_https": "https://pbs.twimg.com/media/C_Udn2UUQAADZIS.jpg",
            "url": "https://t.co/9r69akA484",
            "display_url": "pic.twitter.com/9r69akA484",
            "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
            "type": "photo",
            "sizes": {
              "medium": {
                "w": 1200,
                "h": 900,
                "resize": "fit"
              },
              "small": {
                "w": 680,
                "h": 510,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "large": {
                "w": 2048,
                "h": 1536,
                "resize": "fit"
              }
            }
          },
          {
            "id": 861627474760708096,
            "id_str": "861627474760708096",
            "indices": [
              68,
              91
            ],
            "media_url": "http://pbs.twimg.com/media/C_Udn4nUMAAgcIa.jpg",
            "media_url_https": "https://pbs.twimg.com/media/C_Udn4nUMAAgcIa.jpg",
            "url": "https://t.co/9r69akA484",
            "display_url": "pic.twitter.com/9r69akA484",
            "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
            "type": "photo",
            "sizes": {
              "small": {
                "w": 680,
                "h": 680,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "medium": {
                "w": 1200,
                "h": 1200,
                "resize": "fit"
              },
              "large": {
                "w": 2048,
                "h": 2048,
                "resize": "fit"
              }
            }
          }
        ]
      }
    }