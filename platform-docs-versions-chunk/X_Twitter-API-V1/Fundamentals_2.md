platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview


## Introduction

Standard

All Twitter APIs that return Tweets provide that data encoded using JavaScript Object Notation (JSON). JSON is based on key-value pairs, with named attributes and associated values. These attributes, and their state are used to describe objects.  

At Twitter we serve many objects as JSON, including _Tweets and_ _Users_. These objects all encapsulate core attributes that describe the object. Each Tweet has an author, a message, a unique ID, a timestamp of when it was posted, and sometimes geo metadata shared by the user. Each User has a Twitter name, an ID, a number of followers, and most often an account bio.

With each Tweet we also generate "entity" objects, which are arrays of common Tweet contents such as hashtags, mentions, media, and links. If there are links, the JSON payload can also provide metadata such as the fully unwound URL and the webpage’s title and description.

So, in addition to the text content itself, a Tweet can have over 150 attributes associated with it. Let’s start with an example Tweet:

> 1/ Today we’re sharing our vision for the future of the Twitter API platform![https://t.co/XweGngmxlP](https://t.co/XweGngmxlP)
> 
> — Twitter Dev (@TwitterDev) [April 6, 2017](https://twitter.com/TwitterDev/status/850006245121695744)

  
The following JSON illustrates the structure for these objects and some of their attributes:

      `{   "created_at": "Thu Apr 06 15:24:15 +0000 2017",   "id_str": "850006245121695744",   "text": "1\/ Today we\u2019re sharing our vision for the future of the Twitter API platform!\nhttps:\/\/t.co\/XweGngmxlP",   "user": {     "id": 2244994945,     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "Internet",     "url": "https:\/\/dev.twitter.com\/",     "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ \u2328\ufe0f #TapIntoTwitter"   },   "place": {      },   "entities": {     "hashtags": [           ],     "urls": [       {         "url": "https:\/\/t.co\/XweGngmxlP",         "unwound": {           "url": "https:\/\/cards.twitter.com\/cards\/18ce53wgo4h\/3xo1c",           "title": "Building the Future of the Twitter API Platform"         }       }     ],     "user_mentions": [          ]   } }`