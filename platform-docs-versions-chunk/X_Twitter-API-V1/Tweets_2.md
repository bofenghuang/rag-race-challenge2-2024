platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/overview


## Overview

Standard

The Twitter's standard search API (search/tweets) allows simple queries against the indices of recent or popular Tweets and behaves similarly to, but not exactly like the [Search UI](https://twitter.com/search-advanced) feature available in Twitter mobile or web clients. The Twitter Search API searches against a sampling of recent Tweets published in the past 7 days.

**Auth:** Twitter Oauth 1.0, app-only or app-user  

**Query abilities:** Limited operators for past ~7 days, recreating the search functionality in the Twitter UI.  See [How to build a standard query here](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/guides/build-standard-queries).

Before digging in, it’s important to know that the standard search API is focused on relevance _and not completeness_. This means that some Tweets and users may be missing from search results. If you want to match for completeness you should consider the [premium](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/search/api-reference/get-search-tweets) or [enterprise](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/search/api-reference/premium-search) search APIs.  

A detailed reference on the standard search API endpoint can be found [HERE](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets).