platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/metrics


## Overview

The metrics field allows developers to access public and private engagement metrics for Tweet and media objects. Public metrics are accessible by anyone with a developer account while private metrics are accessible from owned/authorized accounts (definition below). By metrics, we mean the total count of impressions, Retweets, Quote Tweets, likes, replies, video views, video view quartiles, URL and profile link clicks for each Tweet specified in the request. There is also the option to view a breakdown of metrics earned in an organic or promoted context, if the Tweet was promoted as an [Ad](https://ads.twitter.com/).

Public metrics can be requested with [App only Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0) authentication. Non-public metrics can be requested for owned/authorized Tweets only. This means developers are required to authenticate using [OAuth 2.0](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) user context authorization.

**Non-public, organic, and promoted metrics are only available for Tweets that have been created within the last 30 days.  
**