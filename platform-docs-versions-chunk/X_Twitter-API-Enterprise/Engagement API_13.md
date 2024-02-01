platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/guides/selecting-engagement-endpoint


## Selecting an Engagement API Endpoint

The Engagement API provides three distinct endpoints:

* **[Totals](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Totals)** - provides grand totals of select metrics from owned 'owned' or 'unowned' Tweets. Some metrics are available for all Tweets, while others are only available for Tweets published in the last 90 days. Supports 250 Tweets per request.
* **[28 hour](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#28hr)** - provides time-series Engagement metrics for ‘owned’ Tweets from the last 28 hours. Supports 25 Tweets per request.
* **[Historical](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Historical)** \- provides time-series Engagement metrics for up to four consecutive weeks for ‘owned’ Tweets posted since September 1, 2014. Supports 25 Tweets per request.  
     

Each endpoint has its own unique characteristics. Whether you are planning to use all three, or are trying to decide which one best matches your use case, it’s important to understand the differences between them.

Below we introduce some key concepts, further explore the three endpoints, and then present example use cases that map generally to a specific endpoint. Our hope is that this information will help you more efficiently integrate all three, or help you decide which single endpoint best fits your mission.