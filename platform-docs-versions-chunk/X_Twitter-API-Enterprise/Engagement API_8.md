platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/guides/dev-getting-started-engagement-api


### Introduction

The purpose of this documentation is to provide developers an introduction to integrating with the Engagement API. We’ll start off by discussing the ‘whys’ of integrating, then start digging into the technical ‘how’ details.

#### What does the Engagement API provide?

* The Engagement API provides impression and engagement data for any Twitter account’s owned Tweets from the last 90 days, assuming that account has authorized your App to request metrics on their behalf using [3-legged OAuth](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). This powerful, yet easy-to-implement solution gives immediate access to impressions and deep engagements such as URL clicks, #hashtag clicks, and many more.
* The Engagement API provides total aggregate metrics for favorites, Retweets, Quote Tweets, replies, and video views views for any Tweet. This can be used as a powerful way to get basic engagement data about any Tweet or collection of Tweets.
* The Engagement API delivers new value to social listening, marketing, and publishing platforms by allowing customers to measure ROI on Twitter by effectively measuring the performance of content using 15+ performance metrics.
* The Engagement API is a request/response API that allows app developers to send requests with Tweet IDs, desired metrics, and a time frame, for which the API instantly returns data.  
     

#### Why integrate? Example use-cases

* Understand the total reach of your content to see how many people view it. See how many people view videos, click on links, click on hashtags, or install my apps.
* Generate both total and time-series engagement metrics.
* Understand basic engagement metrics (favorites, Retweets, Quote Tweets, replies) about any public Tweet.
* Use these metrics to determine what types of Tweets work so I can post them more often and get more impressions and more engagements for my content.
* Automate marketing behavior (such as Retweeting content from a different owned account) every time one of my Tweets reaches 100 Likes, or another threshold.
* Benchmark and compare my campaigns against each other as a tool for A/B testing.
* Analyze what type of content resonates for my customer service department to determine how and when to respond.
* Show analytics for content that is published from my platform.  
     

The [Engagement API was launched in 2016](https://blog.twitter.com/official/en_us/a/2016/gnip-s-engagement-api-is-now-generally-available.html) and was the first Twitter API to provide these in-depth engagement metrics at scale. The Engagement API is easy to use and enables customers to automate the process. Here is a case study describing an example integration:

* [Measuring campaign success with the Red Cross](https://blog.twitter.com/developer/en_us/topics/spotlight/2016/measuring-campaign-success-with-the-red-cross.html)[](https://simplymeasured.com/blog/true-twitter-impressions-and-url-clicks-new-from-simply-measured/#sm.0007werel134td8zqf02m2mduumr6)

Now that we’ve explored the ‘whys’ of the Engagement API, let’s start digging into the technical details.