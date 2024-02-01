platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/poll-metadata

### Sample Payload

Below is a snippet of the enriched native format payload highlighting the added poll metadata:

    "entities":{  
          "hashtags":[],
          "urls":[],
          "user_mentions":[],
          "symbols":[],
          "polls":[  
             {  
                "options":[  
                   {  
                      "position":1,
                      "text":"The better answer"
                   },
                   {  
                      "position":2,
                      "text":"The best answer"
                   }
                ],
                "end_datetime":"Sat Feb 04 15:33:11 +0000 2017",
                "duration_minutes":1440
             }
          ]
       },

* * *