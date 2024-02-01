platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/introduction


## Introduction

The v2 Tweet counts endpoints allow developers to understand and retrieve the volume of data for a given query.  This can be beneficial for a number of reasons, including:

* Understand the Tweet volume for a keyword to build visualizations, such as trendlines.  
    
* Understanding the time period in which an event or conversation occurred, to ensure your query captures the relevant data
* Understanding how many Tweets a search query will return, in order to refine your query, before using the recent search or full-archive search endpoints.  
    **Please note:** The counts will not always match the result that will be returned from search endpoints because the search endpoints go through additional compliance that the counts endpoints do not go through
* Understanding the size of the conversation around a topic, without actually having to pull the raw data, and put Tweets against your monthly [Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps). 

When developing a query, you will be limited to a certain query length and to specific operators based on your [access level](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level). 

* If you are using a Project with Essential or Elevated access, you can use the core operators to develop your query, and can use queries up to 512 characters in length. 
* If you are using a Project with Academic Research access, you can use all available operators, and use queries up to 1024 characters in length.   
    
* If you are using a Project with Enterprise access, you can use all available operators, and use queries up to 4096 characters in length.   
      
    

You can also specify the granularity (which can be day, hour, or minute) as well as the time period for which you need the Tweet counts (using the start\_time and end\_time parameters). The default time granularity that this endpoint uses is hour, which means if you do not specify the granularity parameter, the endpoint will give you the Tweet counts per hour, for the last 7 days.  

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).