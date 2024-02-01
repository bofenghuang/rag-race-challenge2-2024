platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/guides/interpreting-metrics


### Impressions and engagement data

The Engagement API delivers **organic** impressions and engagement data.

Impressions represent the number of times that a given Tweet has been viewed on the Twitter platform in an organic context. Impressions generated from Tweets that are seen in a Promoted or Paid context are **not** included.

Engagements represent the number of times that a given Tweet was engaged upon by a viewer in both an **organic** and **promoted** context. Engagements include, but are not limited to, Retweets, Favorites, Replies, URL Clicks, Hashtag Clicks, Mention Clicks, and Media Views. For the full list of included engagement actions, please see the Engagement Data section. 

In order to calculate a baseline engagement rate, please use the total number of engagements divided by the total number of impressions for a given Tweet for the time period you are analyzing.  

Impression and engagement data can only be retrieved for Tweets from owned @handles, or @handles that have authorized your application to view details about their Tweets.  Internally, the Engagement API will track the number of unique @handles that have been requested against the contracted @handle limit.  It's recommended to also track the @handle request usage on the client side throughout the month.