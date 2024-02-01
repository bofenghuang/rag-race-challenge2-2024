platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/changelog


### Product overview

The enterprise-tier Full-archive Search was launched in August 2015, and the premium-tier version was launched in February 2018. These search products enable customers to immediately access any publicly available Tweet. With Full-archive Search you submit a single query and receive a response in classic RESTful fashion. Full-archive Search implements (up to) 500-Tweets-per-response pagination, and supports up to a 60-requests-per-minute (rpm) rate-limit for premium, 120 rpm for enterprise. Given these details, Full-archive Search can be used to rapidly retrieve Tweets, and at large scale using concurrent requests.

Unlike Historical PowerTrack, whose archive is based on a set of Tweet flat-files on disk, the Full-archive Search Tweet archive is much like an on-line database. As with all databases, it supports making queries on its contents. It also makes use of an _index_ to enable high-performance data retrieval. With Full-archive search endpoints, the querying language is made up of PowerTrack Operators, and these Operators each correspond to a Tweet JSON attribute that is indexed.

Also, like Historical PowerTrack, there are Tweet attributes that are current to the time a query is made. For example, if you are using Search API to access a Tweet posted in 2010 today, the user's profile description, account 'home' location, display name, and Tweet metrics for Favorites and Retweet counts will be updated to today’s values and not what they were in 2010.