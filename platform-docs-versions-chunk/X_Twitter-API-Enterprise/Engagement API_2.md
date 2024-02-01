platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/overview


## Overview

[Enterprise](https://developer.twitter.com/en/products/twitter-api/enterprise)

_This is an enterprise API available within our managed access levels only. To use this API, you must first set up an account with our enterprise sales team. [Learn more](https://developer.twitter.com/en/docs/twitter-api/enterprise)_  

The Engagement API provides access to Tweet impression and engagement metrics. While most metrics and endpoints require you to authenticate using [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), you can access public Favorite, Retweet, Reply, and Video Views metrics using [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0) and the /totals endpoint.  

**Note:** You may observe differences between reported data on some of the Twitter web dashboards, and the data reported in the Engagement API. These differences occur because the web dashboards typically only show engagements and/or impressions that occurred within the selected time range. For example, a web dashboard may show engagement on Tweets within the span of a calendar month, while the Engagement API may show engagements that fall beyond the span of that month, but within the time range requested. The Engagement API should be seen as the valid source, in these cases.