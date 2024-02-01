platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits


## Overview

Standard

Every day many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, limits are placed on the number of requests that can be made. These limits help us provide the reliable and scalable API that our developer community relies on. 

The maximum number of requests that are allowed is based on a time interval, some specified period or window of time. The most common request limit interval is fifteen minutes. If an endpoint has a rate limit of 900 requests/15-minutes, then up to 900 requests over any 15-minute interval is allowed. 

Rate limits are applied based on which authentication method you are using. For example, if you are using OAuth 1.0a User Context, you will have one limit per time period for each set of users’ access tokens, while if you are using OAuth 2.0 Bearer Token, you will have a separate limit per time period for requests made by your app. When these limits are exceeded, an error is returned. Keep reading to learn more about these details and tips on how to avoid being rate limited.