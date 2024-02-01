platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/extended-entities


## Tweet with native video

Below is the extended entities metadata for this Tweet with a video:

> St. Vrain River @ Crane Hollow [pic.twitter.com/TLSTTOvvmP](https://t.co/TLSTTOvvmP)
> 
> — @FloodSocial demo (@FloodSocial) [May 29, 2017](https://twitter.com/FloodSocial/status/869318041078820864)

    {
      "extended_entities": {
        "media": [
          {
            "id": 869317980307415040,
            "id_str": "869317980307415040",
            "indices": [
              31,
              54
            ],
            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
            "url": "https://t.co/TLSTTOvvmP",
            "display_url": "pic.twitter.com/TLSTTOvvmP",
            "expanded_url": "https://twitter.com/FloodSocial/status/869318041078820864/video/1",
            "type": "video",
            "sizes": {
              "small": {
                "w": 340,
                "h": 604,
                "resize": "fit"
              },
              "large": {
                "w": 720,
                "h": 1280,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "medium": {
                "w": 600,
                "h": 1067,
                "resize": "fit"
              }
            },
            "video_info": {
              "aspect_ratio": [
                9,
                16
              ],
              "duration_millis": 10704,
              "variants": [
                {
                  "bitrate": 320000,
                  "content_type": "video/mp4",
                  "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/vid/180x320/FMei8yCw7yc_Z7e-.mp4"
                },
                {
                  "bitrate": 2176000,
                  "content_type": "video/mp4",
                  "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/vid/720x1280/octt5pFbISkef8RB.mp4"
                },
                {
                  "bitrate": 832000,
                  "content_type": "video/mp4",
                  "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/vid/360x640/2OmqK74SQ9jNX8mZ.mp4"
                },
                {
                  "content_type": "application/x-mpegURL",
                  "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/pl/wcJQJ2nxiFU4ZZng.m3u8"
                }
              ]
            }
          }
        ]
      }
    }

When an advertiser chooses to limit video playback to just Twitter owned and operated platforms, the `video_info` object will be replaced with an `additional_media_info` object.  
  
The `additional_media_info` will contain additional media info provided by the publisher, such as `title`, `description` and `embeddable flag`. Video content is made available only to Twitter official clients when `embeddable=false`. In this case, all video URLs provided in the payload will be Twitter-based, so the user can open the video in a Twitter owned property by clicking the link.  
  
Here is an example of what the extended entities object will look like in this situation:

    {
      "extended_entities": {
        "media": [
          {
            "id": 924685332347469824,
            "id_str": "924685332347469824",
            "indices": [
              49,
              72
            ],
            "media_url": "http://pbs.twimg.com/media/DNUkdLMVwAEzj8K.jpg",
            "media_url_https": "https://pbs.twimg.com/media/DNUkdLMVwAEzj8K.jpg",
            "url": "https://t.co/90xOJqKMox",
            "display_url": "pic.twitter.com/90xOJqKMox",
            "expanded_url": "https://twitter.com/nyjets/status/924685391524798464/video/1",
            "type": "photo",
            "sizes": {
              "small": {
                "w": 680,
                "h": 383,
                "resize": "fit"
              },
              "medium": {
                "w": 1200,
                "h": 675,
                "resize": "fit"
              },
              "large": {
                "w": 1280,
                "h": 720,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              }
            },
            "additional_media_info": {
              "title": "#ATLvsNYJ: Tomlinson TD from McCown",
              "description": "NFL",
              "embeddable": false,
              "monetizable": true
            }
          }
        ]
      }
    }
    

As discussed above, here is the `entities` section that incorrectly has the `type` set to ‘photo’. Again, the `extended_entities` section is preferred for all native media types, including ‘video’ and ‘animated\_gif’.

    {
    "entities": {
        "hashtags": [
          
        ],
        "urls": [
          
        ],
        "user_mentions": [
          
        ],
        "symbols": [
          
        ],
        "media": [
          {
            "id": 869317980307415040,
            "id_str": "869317980307415040",
            "indices": [
              31,
              54
            ],
            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
            "url": "https://t.co/TLSTTOvvmP",
            "display_url": "pic.twitter.com/TLSTTOvvmP",
            "expanded_url": "https://twitter.com/FloodSocial/status/869318041078820864/video/1",
            "type": "photo",
            "sizes": {
              "small": {
                "w": 340,
                "h": 604,
                "resize": "fit"
              },
              "large": {
                "w": 720,
                "h": 1280,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "medium": {
                "w": 600,
                "h": 1067,
                "resize": "fit"
              }
            }
          }
        ]
      }
    
    }