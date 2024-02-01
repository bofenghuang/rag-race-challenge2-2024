platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/overview


## Available data formats

Please note: It is highly recommended to use the [Enriched Native](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html) format for enterprise data APIs. 

* The Enriched Native format includes all new metadata since 2017, such as [poll metadata](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/poll-metadata.html), and additional metrics such as reply\_count and quote\_count.
    
* Activity Streams format has not been updated with new metadata or enrichments since the [character update](https://blog.twitter.com/official/en_us/topics/product/2017/Giving-you-more-characters-to-express-yourself.html) in 2017.
    

Enterprise data APIs deliver data in two different formats.  The enterprise format closest to the standard v1.1 native format is Native Enriched.  The legacy enterprise data format is Activity Streams, orignially implimented and used by Gnip as a normalized format across Twitter and other social media data providers at the time. While this format is still available, Twitter has only invested new features and developments on the native enriched format since 2017.  

The enriched native format is exactly how it sounds, it includes native Twitter objects as well as additional enrichments avialable for enterprise data products such as URL unwinding metadata, profile geo, poll metadata and additional engagement metrics.  

* [Expanded and enhanced URLs enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls)
* [Matching rules enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules)
* [Poll metadata enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/poll-metadata)
* [Profile geo enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo)