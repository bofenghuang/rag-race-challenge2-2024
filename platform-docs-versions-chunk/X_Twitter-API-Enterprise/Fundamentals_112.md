platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules

## PowerTrack

Tweets delivered through PowerTrack (realtime, Replay, and Historical) will contain the matching\_rules object as follows:

      `"matching_rules": [{         "tag": null,         "id": 907728589029646336,         "id_str": "907728589029646336"     }]`
    

  
In PowerTrack, the matching\_rules object reflects _all_ rules that matched the given result. In other words, if more than one rule matches a specific Tweet, it will only be delivered once, but the matching\_rules element will contain all the rules that matched.