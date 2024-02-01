platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/guides/selecting-engagement-endpoint


### Endpoints and example use cases

Given the characteristics and differences discussed above, each individual endpoint generally maps to different types of use cases. To help you decide which endpoint best serves your particular use case, below are some example user statements and the endpoint that best satisfies it.  

#### **/totals**  

* I only need access to some metric types (Impressions, Engagements, Favorites, Retweets, Quote Tweets, Replies, and Video Views).
* I need access to basic engagement data for any Tweet, not just owned Tweets.
* I want to compare performance against a competitor.
* I want to track basic engagement stats for a hashtag or campaign that includes Tweets that I don’t own.
* I don’t need data broken out by day or hour, I just need the current total when I make a request.
* I need a single metric to show in a report or dashboard and don’t want to store any data.
* I want to show data at page load time, and just need to make a request and get a response.
* I need access to get data for hundreds of thousands or millions of Tweets per day.  
     

#### **/28hr**

* I need access to all 17 metric types.
* I want to show data for very recent Tweets posted in last 28 hours.
* I have a job that runs once a day to get data that I care about and only need to get data for the last day.
* I need to have metrics broken out by day or hour.
* I want to show time-series breakouts of activity by hour in a dashboard.
* I need high access for hundreds of thousands to Tweets per day
* I have storage capabilities and can refresh data once per day and keep a running tally.  
     

#### **/historical**

* I need access to all 17 metric types.
* I need to get historical data for Tweets created all the way back to September 2014.
* I want to show detailed historical analysis that compares campaigns.
* I need to have metrics broken out by day or hour.
* I don’t need high access to the Engagement API and only need to get data for a few hundred or thousand Tweets per day.