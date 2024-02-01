platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/overview


## Overview

**Important notice:**  On **June 19, 2019**, we began limiting total GET requests to the v1.1 /statuses/mentions\_timeline and /statuses/user\_timeline endpoints to 100,000 requests per day. This is a total request limit (per endpoint) applied across both user-auth and app-auth requests. This means that in a 24-hour period, a single app can make up to 100,000 requests to /statuses/mentions\_timeline and/or 100,000 requests to /statuses/user\_timeline (with either app or user auth) before hitting this new app-level rate limit. The existing default user-auth and app-auth rate limits remain the same.

A timeline is simply a list, or an aggregated stream of Tweets.  The Twitter API has several endpoints that return a timeline of Tweet data - see the table below for more details:  

| API endpoint | Description |
| --- | --- |
| [GET statuses / home\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-home_timeline) | Returns a collection of the most recent Tweets posted by the authenticating user and the users they follow. |
| [GET statuses / user\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline) | Returns a collection of the most recent Tweets posted by the indicated by the screen\_name or user\_id parameters. |
| [GET statuses/mentions\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-mentions_timeline) | Returns the 20 most recent mentions (Tweets containing a users’s @handle) for the authenticating user. |