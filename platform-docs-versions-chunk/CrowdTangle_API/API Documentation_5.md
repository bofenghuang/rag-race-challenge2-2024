platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/Posts


## [](#get-postid)GET /post/:id

Retrieves a specific post. There are two versions of this endpoint, depending upon what you need. Both return the same data. Please note that you must use a dashboard token that corresponds to the post platform - i.e. an Instagram token for Instagram posts, and a Facebook token for Facebook posts.

Please also note that the ID format for Facebook and Instagram are different. For Instagram, it's `[post_id]_[page_id]`, while for Facebook, it's `[page_id]_[post_id]`. While Page and Post IDs can be found in Facebook post URLs, Instagram does not expose the IDs in its URLs. You can pull the necessary Instagram IDs from our API.

#### [](#endpoint---platform-id)Endpoint - Platform ID

`GET http://api.crowdtangle.com/post/:id`

#### [](#path-variables)Path Variables

| Path Variable | Description |
| --- | --- |
| id  | The ID of the post on its platform which corresponds to the **platformId** property of the Post object. This is provided as a path variable in the URL. For Facebook and Instagram, requires the full \[number\]\_\[number\] ID format. |

#### [](#parameters-1)Parameters

| Parameter | Description |
| --- | --- |
| account | The slug or ID of the posting account on its platform. This is required for Reddit, ignored for Facebook and Instagram (where a post ID contain the account's ID). |
| includeHistory | `null` (does not include) |

#### [](#endpoint---crowdtangle-id)Endpoint - CrowdTangle ID

`GET http://api.crowdtangle.com/ctpost/:id`

#### [](#path-variables-1)Path Variables

| Path Variable | Description |
| --- | --- |
| id  | The CrowdTangle ID of the post which corresponds to the **id** property of the Post object and is represented in the \[number\]\|\[number\] ID format. This is provided as a path variable in the URL. |

#### [](#response-1)Response

The response contains a status code and a result. The result is an array of posts containing a single [post](https://github.com/CrowdTangle/API/wiki/Post).

    // Call: https://api.crowdtangle.com/post/47657117525_10154014482272526?token=TOKEN
    {
        "status": 200,
        "result": {
            "posts": [
                {
                    "platformId": "47657117525_10154014482272526",
                    "platform": "Facebook",
                    "date": "2016-02-12 23:38:14",
                    "updated": "2020-08-23 05:48:22",
                    "type": "live_video_complete",
                    "message": "Draymond at Foot Locker for #NBAAllStarTO with a special shoutout to #DubNation.",
                    "expandedLinks": [
                        {
                            "original": "https://www.facebook.com/warriors/videos/10154014482272526/",
                            "expanded": "https://www.facebook.com/warriors/videos/10154014482272526/"
                        }
                    ],
                    "link": "https://www.facebook.com/warriors/videos/10154014482272526/",
                    "postUrl": "https://www.facebook.com/warriors/posts/10154014482272526",
                    "subscriberCount": 6041837,
                    "score": 4.750579867017164,
                    "media": [
                        {
                            "type": "video",
                            "url": "https://video-sea1-1.xx.fbcdn.net/v/t42.1790-29/12718926_1213464465334694_1083747983_n.mp4?_nc_cat=109&_nc_sid=985c63&efg=eyJybHIiOjQ0MiwicmxhIjoxNDIwLCJ2ZW5jb2RlX3RhZyI6InYyXzQwMF9jcmZfMjdfbWFpbl8zLjBfc2QifQ%3D%3D&_nc_ohc=e7Ygz2qv-24AX-wSWX2&rl=442&vabr=246&_nc_ht=video-sea1-1.xx&oh=889e0d776d92a84bb57099cad3d28d55&oe=5F43C879",
                            "height": 0,
                            "width": 0
                        },
                        {
                            "type": "photo",
                            "url": "https://scontent-sea1-1.xx.fbcdn.net/v/t15.5256-10/12526285_831341603658336_1493677499_n.jpg?_nc_cat=101&_nc_sid=1055be&_nc_ohc=DH0vfblGwtIAX_x8SBs&_nc_ht=scontent-sea1-1.xx&oh=b09d6378fa261fd45345e79c50c254cb&oe=5F696BE1",
                            "height": 400,
                            "width": 400,
                            "full": "https://scontent-sea1-1.xx.fbcdn.net/v/t15.5256-10/12526285_831341603658336_1493677499_n.jpg?_nc_cat=101&_nc_sid=1055be&_nc_ohc=DH0vfblGwtIAX_x8SBs&_nc_ht=scontent-sea1-1.xx&oh=b09d6378fa261fd45345e79c50c254cb&oe=5F696BE1"
                        }
                    ],
                    "statistics": {
                        "actual": {
                            "likeCount": 24235,
                            "shareCount": 753,
                            "commentCount": 5675,
                            "loveCount": 33,
                            "wowCount": 18,
                            "hahaCount": 3,
                            "sadCount": 0,
                            "angryCount": 5,
                            "thankfulCount": 0,
                            "careCount": 0
                        },
                        "expected": {
                            "likeCount": 3927,
                            "shareCount": 279,
                            "commentCount": 1041,
                            "loveCount": 1046,
                            "wowCount": 94,
                            "hahaCount": 45,
                            "sadCount": 14,
                            "angryCount": 19,
                            "thankfulCount": 0,
                            "careCount": 2
                        }
                    },
                    "account": {
                        "id": 19889,
                        "name": "Golden State Warriors",
                        "handle": "warriors",
                        "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/74788912_10158146665972526_3545220405897723904_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=9snUpG_pdlQAX90IhWM&_nc_ht=scontent-sea1-1.xx&tp=6&oh=f8a3d3b62b507966ecc68de3b557fe84&oe=5FBF1185",
                        "subscriberCount": 11580228,
                        "url": "https://www.facebook.com/47657117525",
                        "platform": "Facebook",
                        "platformId": "47657117525",
                        "accountType": "facebook_page",
                        "pageAdminTopCountry": "US",
                        "verified": true
                    },
                    "videoLengthMS": 307968,
                    "liveVideoStatus": "completed",
                    "Id": "19889|10154014482272526",
                    "legacyid": 1686762829
                }
            ]
        }
    }