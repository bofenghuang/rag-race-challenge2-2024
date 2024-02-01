platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search


## Introduction [¶](#introduction- "Permalink to this headline")

There are two enterprise search APIs:

* 30-Day Search API - provides Tweets posted with the last 30 days.
* Full-Archive Search API - provides Tweets from as early as 2006, starting with the first Tweet posted in March 2006.

These search APIs share a common design and the documentation below applies to both. Note that for Tweets created starting September 29, 2022, Tweet objects will include Tweet edit metadata that describes its edit history. See the ["Edit Tweets"](https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets) fundamentals page for more details.

Below you will find important details needed when integrating with the enterprise search APIs:

* Methods for requesting Tweet data and counts
* Authentication
* Pagination
* API request parameters and example requests
* API response JSON payloads and example responses
* HTTP response codes

The enterprise APIs provide low-latency, full-fidelity, query-based access to the Tweet archive. The only difference in the two APIs is the time frame you can search, either the previous 30 days or from as early as 2006. Time frames can be specified with minute granularity. Tweet data is served in reverse chronological order, starting with the most recent Tweet that matches your query. Tweets are available from the search API approximately 30 seconds after being published.