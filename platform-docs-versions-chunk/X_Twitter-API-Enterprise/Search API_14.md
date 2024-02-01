platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/quick-start/enterprise-full-archive

Enterprise Search Tweets: Full-Archive API

## Getting started with enterprise Search Tweets: Full-Archive API

**⏱ 10 min read**

The enterprise Search Tweets: Full-Archive API provides you with Tweets since the first one posted in 2006. Tweets are matched and sent back to you based on the query you specify in your request. A query is a rule in which you define what the Tweet you get back should contain. In this tutorial, we will search for Tweets originating from the Twitter account @TwitterDev in English.

The Tweets you get back in your payload can be in a data format, which provides you with the full Tweet payload, or it can be in a counts format which gives you numerical count data of matched Tweets. We will be using cURL to make requests to the data and counts endpoints.

You will need the following:

* [An enterprise account](https://developer.twitter.com/en/enterprise)
* Your username, password, and account name
* Label associated with your search endpoint, as displayed at console.gnip.com