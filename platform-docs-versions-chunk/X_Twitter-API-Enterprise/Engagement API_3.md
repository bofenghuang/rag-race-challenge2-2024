platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/overview


### Request endpoints

The Engagement API has three endpoints:

#### Current Totals: [/totals](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Totals)

* Requests return a total metric for impressions and a total metric for engagements for the desired Tweets
* Limited to the following metrics: Impressions, Engagements, Favorites, Replies, Retweets, Quote Tweets, and Video Views
* Supports the ability to retrieve **Impressions** and **Engagements** metrics for Tweets created **within the last 90 days** using OAuth 1.0a User Context
* Supports the ability to retrieve **Favorites, Retweets, Quote Tweets, Replies,** and **Video Views** metrics for **any Tweet** using OAuth 2.0 Bearer token
* The results are based on the current total of impressions and engagements at the time the request is made
* Ideal for powering a dashboard report and for calculating engagement rates across a variety of @handles
* Supports requesting metrics for up to 250 Tweets per request  
     

#### Last 28 hours: [/28hr](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#28hr)

* Requests can return a total metric for impressions, a total metric for engagements, and breakdown of individual engagement metrics that have occurred in the last 28 hours
* Data can be grouped by Tweet ID, and in time-series in aggregate, by day, or by hour
* Ideal for tracking the performance of recently created content
* Supports all available metrics
* Supports requesting metrics for up to 25 Tweets per request  
     

#### Historical: [/historical](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Historical)

* Requests can return impressions, engagements, and a breakdown of individual engagement metrics for the most recent one year, based on the engagement time (not the Tweet creation time).
* Requests support a start date and end date parameter, providing flexibility to narrow into a specific time frame up to 4 weeks in duration.
* Tweet engagement data is limited to only 365 days in the past.
* Data can be grouped by Tweet ID, and in time-series in aggregate, by day, or by hour.
* Ideal for evaluating recent performance against a historical benchmark or developing a historical picture of an @handle’s performance.
* Supports all available metrics.
* Supports requesting metrics for up to 25 Tweets per request.