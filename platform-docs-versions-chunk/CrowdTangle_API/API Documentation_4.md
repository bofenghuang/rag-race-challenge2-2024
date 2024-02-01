platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/Posts


## [](#get-posts)GET /posts

Retrieve a set of posts for the given parameters.

#### [](#endpoint)Endpoint

`GET https://api.crowdtangle.com/posts`

#### [](#parameters)Parameters

| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| accounts | `null` (any account in the List or Dashboard) | a string corresponding to account handles (ie iamcardib) or platform IDs (ie 1436859892) | The account handles or platform ids to search. These can be separated by commas to include multiple accounts. |
| brandedContent | `no_filter` e.g. all | `as_publisher`, `as_marketer`, `exclude`, `no_filter` | Limits to or excludes posts that have been marked as Branded Content, either as Publisher or Marketer. |
| count | `10` | `1-100` | The number of posts to return. |
| endDate | now | \-  | The latest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). |
| includeHistory | `null` (does not include) | `true` | Includes timestep data for growth of each post returned. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle. |
| language | `null` (all languages) | [2-character Locale code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) | Exceptions: Some languages require more than two characters: Chinese (Simplified) is zh-CN and Chinese (Traditional) is zh-TW. |
| listIds | `null` (i.e posts from all Lists, not including saved searches or saved posts lists, in the Dashboard) | \-  | The IDs of lists or saved searches to retrieve. These can be separated by commas to include multiple lists. |
| minInteractions | `0` | `> 0` | If set, will exclude posts with total interactions below this threshold. |
| offset | `0` | `> 0` | The number of posts to offset (generally used for pagination). Pagination links will also be provided in the response. |
| pageAdminTopCountry | `null` | [2-character country code](https://en.m.wikipedia.org/wiki/List_of_ISO_3166_country_codes#Current_ISO_3166_country_codes) | Limits to posts for which the account has the pageAdminTopCountry matching the parameter setting. |
| searchTerm | `null` | Any string | Returns only posts that match this search term. Terms AND automatically. Separate with commas for OR, use quotes for phrases. E.g. CrowdTangle API -> AND. CrowdTangle, API -> OR. "CrowdTangle API" -> AND in that exact order. You can also use traditional Boolean search with this parameter. |
| sortBy | `overperforming` | `date`, `interaction_rate`, `overperforming`, `total_interactions`, `underperforming` | The method by which to filter and order posts. |
| startDate | `null` | \-  | The earliest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). This must be before endDate. Timeframe and startDate are mutually exclusive; if both are passed, startDate will be preferred. |
| timeframe | `6 HOUR` | Any valid SQL interval (No, we don't pass it through to our database. Don't be silly) | The interval of time to consider from the endDate. Timeframe and startDate are mutually exclusive; if both are passed, startDate will be preferred. Depending on the number of posts, longer timeframes may not return within the timeout window. If you get a 504, try shortening your timeframe. |
| types | `null` (all) | `album`, `igtv`, `link`, `live_video`, `live_video_complete`, `live_video_scheduled`, `native_video`, `photo`, `status`, `video`, `vine`, `youtube` | The types of post to include. These can be separated by commas to include multiple types. If you want all live videos (whether currently or formerly live), be sure to include both live\_video and live\_video\_complete. The "video" type does not mean all videos, it refers to videos that aren't native\_video or youtube (e.g. a video on Vimeo). |
| verified | `no_filter` (all) | `only`, `exclude`, `no_filter` | Limits to posts where the account has the verified setting matching the input. |
| weightAngry, weightComment, weightHaha, weightLike, weightLove, weightRepost, weightSad, weightShare, weightUpvote, weightView, weightWow | 0   | 0-10 | How much weight to give to each type of interaction. If you send in no weights, all weights will use the current dashboard defaults. If you send in at least one weight, all other weights will default to 0. Weights are multiplied by interaction counts: e.g. weightsComment at 1 and all others at 0 will find the most commented-on posts. weightLike at 1 and weightShare at 2 will give shares twice the impact as likes when computing scores. |

#### [](#response)Response

The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of [post objects](https://github.com/CrowdTangle/API/wiki/Post) and a [pagination object](https://github.com/CrowdTangle/API/wiki/Pagination) with URLs for both the next and previous page, if they exist. Below is an example response.

    // Call: https://api.crowdtangle.com/posts?token=TOKEN&listIds=1310154&sortBy=total_interactions&count=2
    {
        "status": 200,
        "result": {
            "posts": [
                {
                    "platformId": "11430503918_10159078346893919",
                    "platform": "Facebook",
                    "date": "2020-10-29 14:56:05",
                    "updated": "2020-10-29 19:03:44",
                    "type": "photo",
                    "message": "Salió el sol 😎 Ánimo mi gente que hoy es JUERNES!!!! 🕺🏻#Perfecta",
                    "expandedLinks": [
                        {
                            "original": "https://www.facebook.com/luisfonsi/photos/a.74490428918/10159078346893919/?type=3",
                            "expanded": "https://www.facebook.com/luisfonsi/photos/a.74490428918/10159078346893919/?type=3"
                        }
                    ],
                    "link": "https://www.facebook.com/luisfonsi/photos/a.74490428918/10159078346893919/?type=3",
                    "postUrl": "https://www.facebook.com/luisfonsi/posts/10159078346893919",
                    "subscriberCount": 13231210,
                    "score": 55081.0,
                    "media": [
                        {
                            "type": "photo",
                            "url": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-0/p600x600/123184409_10159078346898919_2930797796463495309_o.jpg?_nc_cat=110&ccb=2&_nc_sid=2d5d41&_nc_ohc=K6a18H3Rdd0AX_6WnSi&_nc_ht=scontent-sea1-1.xx&tp=6&oh=f2f8879521dd107979e73ccad9a40260&oe=5FC0E9D8",
                            "height": 719,
                            "width": 600,
                            "full": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-0/p600x600/123184409_10159078346898919_2930797796463495309_o.jpg?_nc_cat=110&ccb=2&_nc_sid=2d5d41&_nc_ohc=K6a18H3Rdd0AX_6WnSi&_nc_ht=scontent-sea1-1.xx&tp=6&oh=f2f8879521dd107979e73ccad9a40260&oe=5FC0E9D8"
                        }
                    ],
                    "statistics": {
                        "actual": {
                            "likeCount": 42617,
                            "shareCount": 303,
                            "commentCount": 1060,
                            "loveCount": 10937,
                            "wowCount": 35,
                            "hahaCount": 123,
                            "sadCount": 4,
                            "angryCount": 2,
                            "thankfulCount": 0,
                            "careCount": 520
                        },
                        "expected": {
                            "likeCount": 10773,
                            "shareCount": 137,
                            "commentCount": 359,
                            "loveCount": 3279,
                            "wowCount": 18,
                            "hahaCount": 16,
                            "sadCount": 2,
                            "angryCount": 2,
                            "thankfulCount": 0,
                            "careCount": 167
                        }
                    },
                    "account": {
                        "id": 11023,
                        "name": "Luis Fonsi",
                        "handle": "luisfonsi",
                        "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/44395322_10156942313018919_1108227336190296064_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=q9kfC3Ks0HcAX-7VZ53&_nc_ht=scontent-sea1-1.xx&tp=6&oh=1f921982b59ade01b6b5907929b2ee30&oe=5FBFC603",
                        "subscriberCount": 13231210,
                        "url": "https://www.facebook.com/11430503918",
                        "platform": "Facebook",
                        "platformId": "11430503918",
                        "accountType": "facebook_page",
                        "pageAdminTopCountry": "US",
                        "verified": true
                    },
                    "Id": "11023|10159078346893919",
                    "legacyid": 110173423951
                },
                {
                    "platformId": "10162931178_10157582304861179",
                    "platform": "Facebook",
                    "date": "2020-10-29 17:00:00",
                    "updated": "2020-10-29 19:07:42",
                    "type": "photo",
                    "expandedLinks": [
                        {
                            "original": "https://www.facebook.com/tobymac/photos/a.241173571178/10157582303601179/?type=3",
                            "expanded": "https://www.facebook.com/tobymac/photos/a.241173571178/10157582303601179/?type=3"
                        }
                    ],
                    "link": "https://www.facebook.com/tobymac/photos/a.241173571178/10157582303601179/?type=3",
                    "postUrl": "https://www.facebook.com/tobymac/posts/10157582304861179",
                    "subscriberCount": 5043407,
                    "score": 52888.0,
                    "media": [
                        {
                            "type": "photo",
                            "url": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-9/p720x720/123164065_10157582303606179_1644220515968605599_o.jpg?_nc_cat=102&ccb=2&_nc_sid=8024bb&_nc_ohc=xzqACcCLEjwAX9l86ZA&_nc_ht=scontent-sea1-1.xx&tp=6&oh=cf86ece71d72344058e2115fdcfb7de2&oe=5FC1563B",
                            "height": 720,
                            "width": 720,
                            "full": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-9/p720x720/123164065_10157582303606179_1644220515968605599_o.jpg?_nc_cat=102&ccb=2&_nc_sid=8024bb&_nc_ohc=xzqACcCLEjwAX9l86ZA&_nc_ht=scontent-sea1-1.xx&tp=6&oh=cf86ece71d72344058e2115fdcfb7de2&oe=5FC1563B"
                        }
                    ],
                    "statistics": {
                        "actual": {
                            "likeCount": 22509,
                            "shareCount": 15651,
                            "commentCount": 383,
                            "loveCount": 14248,
                            "wowCount": 58,
                            "hahaCount": 9,
                            "sadCount": 29,
                            "angryCount": 1,
                            "thankfulCount": 0,
                            "careCount": 410
                        },
                        "expected": {
                            "likeCount": 11644,
                            "shareCount": 5123,
                            "commentCount": 280,
                            "loveCount": 5404,
                            "wowCount": 9,
                            "hahaCount": 4,
                            "sadCount": 8,
                            "angryCount": 2,
                            "thankfulCount": 0,
                            "careCount": 190
                        }
                    },
                    "account": {
                        "id": 20656,
                        "name": "TobyMac",
                        "handle": "tobymac",
                        "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/96034089_10157131542946179_1640202341955141632_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=qy0yJDS2mAQAX_jqKlW&_nc_ht=scontent-sea1-1.xx&tp=6&oh=8b8c02a81a13632fdb4b1340abdba255&oe=5FC170E9",
                        "subscriberCount": 5043407,
                        "url": "https://www.facebook.com/10162931178",
                        "platform": "Facebook",
                        "platformId": "10162931178",
                        "accountType": "facebook_page",
                        "pageAdminTopCountry": "US",
                        "verified": true
                    },
                    "imageText": "2 the trees are about to show us how lovely it is to let things go tOBYMAC #SPEAKLIFE",
                    "Id": "20656|10157582304861179",
                    "legacyid": 110181321374
                }
            ],
            "pagination": {
                "nextPage": "https://api.crowdtangle.com/posts?token=TOKEN&sortBy=total_interactions&endDate=2020-10-29T19:21&startDate=2020-10-29T13:21:06&listIds=1310154&searchField=TEXT_FIELDS_AND_IMAGE_TEXT&count=2&offset=2"
            }
        }
    }