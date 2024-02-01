platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls


### Tweet payload

The Expanded and Enhanced URL enrichment can be found within the `entities` object of the Tweet payload - specifically in the `entitites.urls.unwound` object. It provides the following fields of metadata:

* Expanded URL - `unwound.url`
* Expanded HTTP Status - `unwound.status`
* Expanded URL HTML title - 300 character limit - `unwound.title`
* Expanded URL HTML description - 1000 character limit - `unwound.description`

  
**This is an example of an [entities object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) with the URL enrichment:**

      `"entities": {     "hashtags": [            ],     "urls": [       {         "url": "https:\/\/t.co\/HkTkwFq8UT",         "expanded_url": "http:\/\/bit.ly\/2wYTb9y",         "display_url": "bit.ly\/2wYTb9y",         "unwound": {           "url": "https:\/\/www.forbes.com\/sites\/laurencebradford\/2016\/12\/08\/11-websites-to-learn-to-code-for-free-in-2017\/",           "status": 200,           "title": "11 Websites To Learn To Code For Free In 2017",           "description": "It\u2019s totally possible to learn to code for free...but what are the best resources to achieve that? Here are 11 websites where you can get started."         },         "indices": [           10,           33         ]       }     ],     "user_mentions": [            ],     "symbols": [            ]   },`
    

  
**This is an example of an entities object containing a Tweet link that is not enriched:  
**

      `"entities": {   "urls": [{      "url": "https://t.co/SywNbZdDmb",      "expanded_url": "https://twitter.com/TwitterDev/status/1050118621198921728",      "display_url": "twitter.com/TwitterDev/s…",      "indices": [          142,          165      ]    }   ] }`