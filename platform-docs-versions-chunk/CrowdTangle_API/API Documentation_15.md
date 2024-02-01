platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/List-Accounts


## [](#get-listslistidaccounts)GET /lists/:listId/accounts

Retrieve the accounts for a given list. Accounts may only be retrieved for [lists](https://github.com/CrowdTangle/API/wiki/List) of type `LIST`, as saved searches and saved posts do not have associated accounts.

#### [](#endpoint)Endpoint

`GET https://api.crowdtangle.com/lists/:listId/accounts` (note that :listID is a placeholder for the actual List ID)

#### [](#path-variables)Path Variables

| Path Variable | Options | Description |
| --- | --- | --- |
| :listId | int | The id of the list for which to retrieve accounts. This is provided as a path variable in the URL. |

#### [](#parameters)Parameters

| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| count | `10` | `1-100` | The number of accounts to return. |
| offset | `0` | `>= 0` | The number of accounts to offset (generally used for pagination). Pagination links will also be provided in the response. |

#### [](#response)Response

The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of [account](https://github.com/CrowdTangle/API/wiki/Account) objects as well as pagination.

    //Call: https://api.crowdtangle.com/lists/73928/accounts?token=TOKEN
    {
        "status": 200,
        "result": {
            "accounts": [
                {
                    "id": 599177,
                    "name": "102.3 FM",
                    "handle": "102.3oficial",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/80087839_10156959736320756_6094224427388502016_n.png?_nc_cat=104&ccb=2&_nc_sid=dbb9e7&_nc_ohc=EU8CreSOPHEAX9hIp8D&_nc_ht=scontent-sea1-1.xx&oh=7b6950783794fdc724e0f4db6d16376d&oe=5FC188F0",
                    "subscriberCount": 76531,
                    "url": "https://www.facebook.com/219679725755",
                    "platform": "Facebook",
                    "platformId": "219679725755",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "BR",
                    "verified": true
                },
                {
                    "id": 350212,
                    "name": "1 NEWS Sport",
                    "handle": "1NEWSSportNZ",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/84670284_2748436965204409_1817888033798619136_o.jpg?_nc_cat=104&ccb=2&_nc_sid=dbb9e7&_nc_ohc=0Qx-7jQ7uQMAX9dFON4&_nc_ht=scontent-sea1-1.xx&tp=6&oh=cc940281a14f4d8b47c64aaf44bc0c6f&oe=5FC24AC1",
                    "subscriberCount": 491559,
                    "url": "https://www.facebook.com/122959744418824",
                    "platform": "Facebook",
                    "platformId": "122959744418824",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "NZ",
                    "verified": true
                },
                {
                    "id": 3197681,
                    "name": "92 Rádio",
                    "handle": "92radio",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/99257503_722143998557016_8827713529218859008_n.png?_nc_cat=103&ccb=2&_nc_sid=dbb9e7&_nc_ohc=8r4QxU6sRMcAX_DqkaD&_nc_ht=scontent-sea1-1.xx&oh=d58aff39f73b1f48e9f33354a87078f9&oe=5FC22EC1",
                    "subscriberCount": 371061,
                    "url": "https://www.facebook.com/142034879901267",
                    "platform": "Facebook",
                    "platformId": "142034879901267",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "BR",
                    "verified": true
                },
                {
                    "id": 103875,
                    "name": "1 NEWS",
                    "handle": "1NEWSNZ",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/83740946_10156915024251218_5477944535067656192_o.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=C-MytOLfteYAX91gnog&_nc_ht=scontent-sea1-1.xx&tp=6&oh=f2a50999c0973deb3d5e7e6d15b571cc&oe=5FBED15B",
                    "subscriberCount": 860358,
                    "url": "https://www.facebook.com/179995481217",
                    "platform": "Facebook",
                    "platformId": "179995481217",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "NZ",
                    "verified": true
                },
                {
                    "id": 890542,
                    "name": "180graus",
                    "handle": "portal180",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/21317492_1550607891667164_6010646426118565060_n.png?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=L4KDOPydKawAX8s6P3U&_nc_ht=scontent-sea1-1.xx&oh=54d627c3a9f0f29d47a008422166ecd6&oe=5FC11277",
                    "subscriberCount": 498309,
                    "url": "https://www.facebook.com/133619913365976",
                    "platform": "Facebook",
                    "platformId": "133619913365976",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "BR",
                    "verified": false
                },
                {
                    "id": 125506,
                    "name": "3al6ayer على الطاير",
                    "handle": "3al6ayer",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/998336_681411518551934_1908797493_n.jpg?_nc_cat=102&ccb=2&_nc_sid=dbb9e7&_nc_ohc=lvNmqMEq_xIAX_TGB5O&_nc_ht=scontent-sea1-1.xx&tp=6&oh=088d3ca604cc66319bd182957c429d91&oe=5FC1FD04",
                    "subscriberCount": 165400,
                    "url": "https://www.facebook.com/167202989972792",
                    "platform": "Facebook",
                    "platformId": "167202989972792",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "SA",
                    "verified": false
                },
                {
                    "id": 73861,
                    "name": "7NEWS Brisbane",
                    "handle": "7NEWSBrisbane",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/110153825_3519595848053242_4551573958521464986_o.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=J4dfl6cHW9gAX_8Rqo4&_nc_ht=scontent-sea1-1.xx&tp=6&oh=d807f3b3de789deb0e5eeb8dea2635ef&oe=5FBF3622",
                    "subscriberCount": 879485,
                    "url": "https://www.facebook.com/130736376939223",
                    "platform": "Facebook",
                    "platformId": "130736376939223",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "AU",
                    "verified": true
                },
                {
                    "id": 370544,
                    "name": "20minutos.es",
                    "handle": "20minutos.es",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/101918673_10158805078443028_8487187545371705344_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=eAgajQdoI6QAX8tpvjc&_nc_ht=scontent-sea1-1.xx&tp=6&oh=3d97d06c47b5bdc49d32b7639f1ef9bc&oe=5FC0ADE7",
                    "subscriberCount": 1182770,
                    "url": "https://www.facebook.com/38352573027",
                    "platform": "Facebook",
                    "platformId": "38352573027",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "ES",
                    "verified": true
                },
                {
                    "id": 126940,
                    "name": "8视界新闻新加坡 8world News",
                    "handle": "8worldnews",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/67619567_2718618618156437_1151093394726977536_o.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=gTsIUOT20AEAX8xZruI&_nc_ht=scontent-sea1-1.xx&tp=6&oh=e1cade89b1c644d32f186b4fd5599c0e&oe=5FBFDD41",
                    "subscriberCount": 541283,
                    "url": "https://www.facebook.com/140711089280549",
                    "platform": "Facebook",
                    "platformId": "140711089280549",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "SG",
                    "verified": true
                },
                {
                    "id": 126958,
                    "name": "7NEWS Australia",
                    "handle": "7NewsAustralia",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/112317767_4000945319915631_7312856053571991158_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=Rs8hBtmGC2UAX_TBxSR&_nc_ht=scontent-sea1-1.xx&tp=6&oh=9328967efcc8f1d6fac13d5773ba3fb0&oe=5FBFE517",
                    "subscriberCount": 2058247,
                    "url": "https://www.facebook.com/114503341893201",
                    "platform": "Facebook",
                    "platformId": "114503341893201",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "AU",
                    "verified": true
                }
            ],
            "pagination": {
                "nextPage": "https://api.crowdtangle.com/lists/:listId/accounts?token=TOKEN"
            }
        }
    }